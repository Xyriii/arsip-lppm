import re
from pathlib import Path
from django.core.management.base import BaseCommand
from django.core.files import File
from arsip.models import Folder, Arsip


# Mapping kedalaman folder ke level
LEVEL_BY_DEPTH = {
    0: 'fonds',
    1: 'subfonds',
    2: 'series',
    3: 'file',
}

# Extension yang didukung
DEFAULT_EXTENSIONS = ('.pdf', '.xlsx', '.xls', '.docx', '.doc', '.jpg', '.jpeg', '.png')


class Command(BaseCommand):
    help = 'Import arsip massal dari folder lokal'

    def add_arguments(self, parser):
        parser.add_argument('source_path', type=str, help='Path folder sumber')
        parser.add_argument('--dry-run', action='store_true', help='Simulasi aja')
        parser.add_argument(
            '--extensions',
            type=str,
            default=','.join(DEFAULT_EXTENSIONS),
            help='Ekstensi file (pisah koma)'
        )

    def handle(self, *args, **options):
        source = Path(options['source_path'])
        dry_run = options['dry_run']
        extensions = tuple(e.strip().lower() for e in options['extensions'].split(','))

        if not source.exists():
            self.stdout.write(self.style.ERROR(f'Folder gak ditemukan: {source}'))
            return

        self.stdout.write(self.style.WARNING(f'Mulai import dari: {source}'))
        if dry_run:
            self.stdout.write(self.style.WARNING('DRY RUN - gak ada yang disimpan'))
        self.stdout.write('')

        stats = {
            'folders_created': 0,
            'folders_existing': 0,
            'files_uploaded': 0,
            'files_skipped': 0,
            'errors': [],
        }

        # Mulai scan
        self.scan(source, parent=None, depth=0, extensions=extensions,
                  dry_run=dry_run, stats=stats)

        # Print hasil
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('=' * 50))
        self.stdout.write(self.style.SUCCESS('SELESAI!'))
        self.stdout.write(self.style.SUCCESS('=' * 50))
        self.stdout.write(f"Folder dibuat   : {stats['folders_created']}")
        self.stdout.write(f"Folder existing : {stats['folders_existing']}")
        self.stdout.write(f"File di-upload  : {stats['files_uploaded']}")
        self.stdout.write(f"File di-skip    : {stats['files_skipped']}")

        if stats['errors']:
            self.stdout.write('')
            self.stdout.write(self.style.ERROR(f"Errors ({len(stats['errors'])}):"))
            for err in stats['errors'][:20]:
                self.stdout.write(self.style.ERROR(f"  - {err}"))

    def scan(self, folder_path, parent, depth, extensions, dry_run, stats):
        """Scan folder rekursif"""
        level = LEVEL_BY_DEPTH.get(depth, 'item')
        folder_name = folder_path.name
        year = self.extract_year(folder_name)

        # Bikin Folder di database
        folder_obj = None
        if not dry_run:
            folder_obj, created = Folder.objects.get_or_create(
                name=folder_name,
                parent=parent,
                defaults={'level': level, 'year': year}
            )
            if created:
                stats['folders_created'] += 1
                self.stdout.write(self.style.SUCCESS(f"  + [{level}] {folder_name}"))
            else:
                stats['folders_existing'] += 1
                self.stdout.write(f"  = [{level}] {folder_name} (existing)")
        else:
            self.stdout.write(f"  [dry] [{level}] {folder_name}")

        # Iterasi isi folder
        items = sorted(folder_path.iterdir(), key=lambda p: (p.is_file(), p.name))

        for item in items:
            if item.is_dir():
                self.scan(item, folder_obj, depth + 1, extensions, dry_run, stats)
            elif item.is_file():
                if item.suffix.lower() not in extensions:
                    stats['files_skipped'] += 1
                    continue
                self.import_file(item, folder_obj, dry_run, stats)

    def import_file(self, file_path, folder, dry_run, stats):
        """Import 1 file"""
        if dry_run:
            stats['files_uploaded'] += 1
            self.stdout.write(f"      [dry] {file_path.name}")
            return

        if folder is None:
            stats['files_skipped'] += 1
            return

        # Cek duplikat
        if Arsip.objects.filter(name=file_path.stem, folder=folder).exists():
            stats['files_skipped'] += 1
            self.stdout.write(f"      = {file_path.name} (skip duplikat)")
            return

        try:
            ext = file_path.suffix.lower().lstrip('.')
            if ext in ('xlsx', 'xls'):
                file_type = 'xlsx'
            elif ext in ('docx', 'doc'):
                file_type = 'docx'
            elif ext == 'pdf':
                file_type = 'pdf'
            else:
                file_type = 'lain'

            arsip = Arsip(
                name=file_path.stem,
                folder=folder,
                file_type=file_type,
                size_bytes=file_path.stat().st_size,
            )
            with open(file_path, 'rb') as f:
                arsip.file.save(file_path.name, File(f), save=True)

            stats['files_uploaded'] += 1
            self.stdout.write(self.style.SUCCESS(f"      + {file_path.name}"))

        except Exception as e:
            stats['errors'].append(f"{file_path.name}: {e}")
            self.stdout.write(self.style.ERROR(f"      x {file_path.name}: {e}"))

    def extract_year(self, name):
        """Extract tahun dari nama folder"""
        match = re.search(r'\b(19|20)\d{2}\b', name)
        return int(match.group()) if match else 2020