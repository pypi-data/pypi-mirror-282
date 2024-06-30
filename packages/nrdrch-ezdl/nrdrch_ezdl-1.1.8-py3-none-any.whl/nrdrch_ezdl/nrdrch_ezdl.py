import os, sys, subprocess, toml, filecmp, re
from rich.console import Console
from rich import print as rprint
from rich import box
from rich.table import Table
from rich.spinner import Spinner
from shutil import copyfile
from datetime import datetime
VERSION_ID = "v1.1.8"

console = Console()
script_dir = os.path.dirname(__file__)
# Define the path for settings.toml
settings_path = os.path.join(os.path.dirname(__file__), 'settings.toml')
version_file = os.path.join(os.path.dirname(__file__), f'{VERSION_ID}')
timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
settings_backup = os.path.join(os.path.dirname(__file__), f'settings_backup_{timestamp}.toml')

default_settings = {
    "paths": {
        "audio_vault_path": r"~\ezdl\Audio",
        "video_vault_path": r"~\ezdl\Video"
    },
    "settings": {
        "audio_quality": "0",
        "audio_format": "wav",
        "video_format": "mp4",
        "file_naming_scheme": "%(title)s - %(duration)s",
        "open_folder_after_download": "no",
        "use_original_thumbnail": "no"
    },
    "aliases": {
        "audio_download_alias": "audio",
        "video_download_alias": "video",
        "audio_open_alias": "audio",
        "video_open_alias": "video",
        "settings_open_alias": "settings"
    },
    "other": {
        "loading_animation": "aesthetic"
    }
}
def create_default_settings():
    with open(settings_path, 'w', encoding='utf-8') as f:
         toml.dump(default_settings, f)
def merge_settings(default, current):
    """Merge missing keys from default settings into current settings."""
    for key, value in default.items():
        if key not in current:
            current[key] = value
        elif isinstance(value, dict):
            merge_settings(value, current[key])
    return current

# Create settings.toml only if it does not exist
if not os.path.exists(settings_path):
    create_default_settings()

# Create version file if it doesn't exist
if not os.path.exists(version_file):
    # Backup the current settings
    copyfile(settings_path, settings_backup)
    os.remove(settings_path)
    create_default_settings()

    with open(version_file, 'w'):
        pass
    console.print(f":party_popper: Version [bold cyan]{VERSION_ID}[/bold cyan] installed! ")

    # Load settings from files
    # Load settings from files
    with open(settings_backup, 'r', encoding='utf-8') as f:
        current_settings = toml.load(f)
    # Compare and merge settings
    updated_settings = merge_settings(default_settings, current_settings)
    # Save updated settings
    # Save updated settings
    with open(settings_path, 'w', encoding='utf-8') as f:
        toml.dump(updated_settings, f)
    if not filecmp.cmp(os.path.normpath(settings_path), os.path.normpath(settings_backup), shallow=False):
        console.print(":warning: [bold red] Warning:[/bold red] The default settings changed!")
        console.print(f"[bold white]BACKUP PATH: [/bold white] [bold yellow]{os.path.normpath(settings_backup)}[/bold yellow]")
        console.print("")


# Load settings from settings.toml
with open(settings_path, 'r', encoding='utf-8') as f:
    settings = toml.load(f)
AUDIO_FORMAT = settings['settings']['audio_format']
VIDEO_FORMAT = settings['settings']['video_format']
SPINNER = settings['other']['loading_animation']
AUDIO_ALIAS = settings['aliases']['audio_download_alias']
VIDEO_ALIAS = settings['aliases']['video_download_alias']
AUDIO_OPEN_ALIAS = settings['aliases']['audio_open_alias']
VIDEO_OPEN_ALIAS = settings['aliases']['video_open_alias']
SETTINGS_OPEN_ALIAS = settings['aliases']['settings_open_alias']
EMBED_THUMBNAILS = settings['settings']['use_original_thumbnail']
OPEN_AFTER_DL = settings['settings']['open_folder_after_download']

# Function to expand PowerShell variables
def expand_powershell_variables(value):
    if isinstance(value, str) and value.startswith('$'):
        # Extract variable name
        var_name = value[1:]  # Remove '$' prefix
        if var_name.startswith('env:'):
            var_name = var_name[4:]  # Remove 'env:' prefix for environment variables

            return os.path.expandvars(f'%{var_name}%')  # Expand environment variables for Windows
        else:
            # Retrieve the value of the PowerShell variable from the environment
            custom_value = os.getenv(var_name)
            if custom_value is not None:
                return custom_value
            else:
                return value  # Return original value if variable not found
    return value  # Return unchanged if not starting with '$'
# Function to handle path expansion based on type
def expand_path(value):
    if isinstance(value, str):
        return expand_powershell_variables(value)
    else:
        return value
AU_PATH = expand_path(os.path.expanduser(settings['paths']['audio_vault_path']))
VID_PATH = expand_path(os.path.expanduser(settings['paths']['video_vault_path']))
def execute_command(command, link, with_playlist):
    command = command.replace("{audio_vault_path}", AU_PATH)
    command = command.replace("{video_vault_path}", VID_PATH)
    command = command.replace("{audio_quality}", settings['settings']['audio_quality'])
    command = command.replace("{audio_format}", settings['settings']['audio_format'])
    command = command.replace("{video_format}", settings['settings']['video_format'])
    command = command.replace("{naming_scheme}", settings['settings']['file_naming_scheme'])
    command = command.replace("<youtube_link>", link)
    if with_playlist:
        command = command.replace('--no-playlist', '')
    if sys.argv[1] == AUDIO_ALIAS:
        if EMBED_THUMBNAILS == 'yes': 
            if AUDIO_FORMAT in ['mp3', 'flac', 'opus', 'ogg', 'mka', 'm4a', 'mov']:
                command = command.replace("{embed_thumbnails}", '--embed-thumbnail')
            else: 
                console.print(f":x:[bold red] log [/bold red]filetype: [bold yellow]{AUDIO_FORMAT}[/bold yellow] does not support thumbnail embedding. Audio filetypes with support: 'mp3', 'flac', 'opus', 'mka', 'mov' & 'ogg'")
                console.print(f":bulb: Note, to get the best quality possible, while also embedding thumbnails, use the 'flac' audio format.")
                return 
        elif EMBED_THUMBNAILS == 'no': 
            command = command.replace("{embed_thumbnails}", '')
    elif sys.argv[1] == VIDEO_ALIAS:
        if EMBED_THUMBNAILS == 'yes': 
            if VIDEO_FORMAT in ['mp4', 'm4v', 'mov']:
                command = command.replace("{embed_thumbnails}", '--embed-thumbnail')
            else: 
                console.print(f":x:[bold red] log [/bold red]filetype: [bold yellow]{VIDEO_FORMAT}[/bold yellow] does not support thumbnail embedding. Video filetypes with support: 'mkv', 'mp4', 'm4v' & 'mov'")
                return 
        elif EMBED_THUMBNAILS == 'no': 
            command = command.replace("{embed_thumbnails}", '')
    with console.status("[bold cyan]Downloading[/bold cyan]", spinner=f"{SPINNER}", spinner_style="status.spinner", speed=1.0, refresh_per_second=12.5):
        try:
            result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True, encoding='utf-8', errors='ignore')
            if result.returncode == 0:
                console.print(":heavy_check_mark:[bold green]  log [/bold green]Download complete!")
                return True
            else:
                console.print(f":x:[bold red] log [/bold red]{result.stderr}")
                return False
        except Exception as e:
            console.print(f":x:[bold red] log [/bold red]{str(e)}")
            return False
def main():
    import sys
    if len(sys.argv) < 2:
        console.print(":x:[bold red] log [/bold red]No arguments provided. Use '--help' or '-h' for usage information.")
        return
    if sys.argv[1] in ['--help', '-h']:
        console.print("[bold white]yt-dlp wrapper for simplicity.[/bold white]" f":wrench: [#A0A0A0]Version[/#A0A0A0] [bold cyan]{VERSION_ID}[/bold cyan]" "\n"
                      "[bold cyan]Usage:[/bold cyan]\n"
                      " [#076841]ezdl [/#076841]" f"{AUDIO_ALIAS}" " <[#DBC75D]link[/#DBC75D]> \n"
                      " [#076841]ezdl [/#076841]" f"{VIDEO_ALIAS}" " <[#DBC75D]link[/#DBC75D]> \n"
                      "\n"
                      "[bold white]optionally run with[/bold white] [#DBC75D]'wp'[/#DBC75D] [bold white]or[/bold white] [#DBC75D]'withplaylist'[/#DBC75D][bold white], to download the whole playlist:[/bold white]\n"
                      " [#076841]ezdl [/#076841]" f"{AUDIO_ALIAS}" " <[#DBC75D]link[/#DBC75D]> [#DBC75D]wp[/#DBC75D] \n"
                      " [#076841]ezdl [/#076841]" f"{VIDEO_ALIAS}" " <[#DBC75D]link[/#DBC75D]> [#DBC75D]wp[/#DBC75D] \n"
                      "\n"
                       "[bold white]navigate to locations with:[/bold white]\n"
                      " [#076841]ezdl [/#076841]open [#DBC75D]" f"{SETTINGS_OPEN_ALIAS}" "[/#DBC75D], [#DBC75D]" f"{AUDIO_OPEN_ALIAS}" "[/#DBC75D] or [#DBC75D]"f"{VIDEO_OPEN_ALIAS}""[/#DBC75D] \n"
                      "\n"
                      "[bold white]Display helpful Information:[/bold white]\n"
                      " [#076841]ezdl [/#076841][#DBC75D]--help[/#DBC75D]  or [#DBC75D] -h [/#DBC75D] \n"
                      "[bold white]More helpful Information about settings:[/bold white]\n"
                      " [#076841]ezdl [/#076841][#DBC75D]--help-settings[/#DBC75D]  or [#DBC75D] -hs [/#DBC75D] "
                      "\n"
                      "[bold cyan]Locations:[/bold cyan]\n"
                      ":gear:  [#A0A0A0]Settings [/#A0A0A0]" f"'{settings_path}'\n"
                      ":musical_note: [#A0A0A0]Audio    [/#A0A0A0]" f"'{os.path.expanduser(AU_PATH)}'" "\n"             
                      ":movie_camera: [#A0A0A0]Video    [/#A0A0A0]" f'"{os.path.expanduser(VID_PATH)}"' ""        
                      )
        return
    if sys.argv[1] in ['--help-settings', '-hs']:
        try:
            with open(settings_path, 'r', encoding='utf-8') as f:
                settings = toml.load(f)

            table = Table(show_header=True, header_style="bold cyan", box=box.SIMPLE_HEAD)
            table.add_column("Setting", style="magenta", justify="left", width=45)
            table.add_column("Description", style="#189255", justify="left", width=57)
            table.add_column("Options & Usage Examples", style="bold white", justify="left", width=96)

            for section, values in settings.items():
                for key, value in values.items():
                    description, options = get_setting_description(section, key)
                    table.add_row(f"{key} = {value}", description, options)

            console.print(table)

        except Exception as e:
            console.print(f":x:[bold red] Exception! [/bold red] {str(e)}")
        return

    
    if len(sys.argv) < 3:

        console.print(":x:[bold red] log [/bold red]Invalid number of arguments. Use '--help' or '-h' for usage information.")
        return
    alias = sys.argv[1]
    if alias == 'open':
        target = sys.argv[2] if len(sys.argv) > 2 else ''
        if target == f'{SETTINGS_OPEN_ALIAS}':
            path = settings_path
        elif target == f'{AUDIO_OPEN_ALIAS}':
            path = path = AU_PATH
        elif target == f'{VIDEO_OPEN_ALIAS}':
            path = VID_PATH
        else:
            console.print("[bold red]:x:[/bold red] Unknown target for open command.")
            return
        try:
            path = os.path.expanduser(os.path.normpath(path))
            if not os.path.exists(path):
                os.makedirs(path)
                console.print(f":wrench: Creating [bold yellow]{path}[/bold yellow] since it didn't exist yet.")
            if os.name == 'nt':  # Windows
                subprocess.run(['explorer', path])
            elif os.name == 'posix':  # macOS and Linux
                subprocess.run(['open' if sys.platform == 'darwin' else 'xdg-open', path])
            console.print(f":heavy_check_mark: [bold green] log [/bold green]Opened path at [bold yellow]{path}[/bold yellow]")
        except Exception as e:
            console.print(f"[bold red]:x: Exception![/bold red] {str(e)}")
        return
    link = sys.argv[2]
    with_playlist = len(sys.argv) > 3 and (sys.argv[3] in ['wp', 'withplaylist'])
    if alias == f'{AUDIO_ALIAS}':
        command = '$null = yt-dlp -x --audio-quality {audio_quality} --audio-format {audio_format} --ignore-errors {embed_thumbnails} --output "{audio_vault_path}\\{naming_scheme}" --no-playlist "<youtube_link>"'
        openpath = os.path.normpath(os.path.expanduser(AU_PATH))
    elif alias == f'{VIDEO_ALIAS}':
        command = '$null = yt-dlp --ignore-errors {embed_thumbnails} --remux-video {video_format} --output "{video_vault_path}\\{naming_scheme}" --no-playlist "<youtube_link>"'
        openpath = os.path.normpath(os.path.expanduser(VID_PATH))
    else:
        console.print(":x:[bold red] log [/bold red]Unknown alias.")
        return
    try:
        if execute_command(command, link, with_playlist):
            if OPEN_AFTER_DL == 'yes':
                if not os.path.exists(openpath):
                    os.makedirs(openpath)
                subprocess.run(['explorer', openpath])
                console.print(f":heavy_check_mark: [bold green] log [/bold green]Opened path at [bold yellow]{openpath}[/bold yellow]")
    except Exception as e:
        console.print(f":x:[bold red] Exception! [/bold red] {str(e)}")

def get_setting_description(section, key):
    descriptions = {
        'paths': {
            'audio_vault_path': ('Audio [red]save[/ red] location.', r'Set [yellow]Path[/yellow] with doubled right-slashes ("[bold green] \\ [/bold green]") [red]OR[/red] single left-slashes ("[bold green] / [/bold green]")  [red]OR[/red] set a [yellow]Variable[/yellow] by full name.'),
            'video_vault_path': ("Video [red]save[/ red] location.", r'[#A0A0A0]To define [/#A0A0A0][yellow]variables[/yellow], [#A0A0A0]run this to open PSProfile[/#A0A0A0]: [yellow]notepad[/yellow] [green]$PROFILE[/green] ; define in normal path-format: [green]$env:yourvarname[/green] = "WindowsPathToDir" '),
        },
        'settings': {
            'audio_quality': ('Audio [red]quality[/red] level', '[green]0[/green] - [red]10[/red] ([bold yellow]10[/bold yellow] = [bold red]worst[/bold red]) '),
            'audio_format': ('Select preffered [red]file format[/red] for Audio.', "[green]wav[/green][bold white],[/bold white] [green]flac[/green][bold white],[/bold white] [yellow]mp3[/yellow][bold white],[/bold white] [yellow]opus[/yellow][bold white],[/bold white] [yellow]ogg[/yellow][bold white],[/bold white][yellow] mka[/yellow][bold white],[/bold white] [yellow]m4a[/yellow][bold white] or [/bold white][yellow]mov[/yellow]"),
            'video_format': ('Select preffered [red]file format[/red] for Video.', "[green]mp4[/green][bold white],[/bold white] [green]m4v[/green][bold white] or[/bold white] [yellow]mov[/yellow]"),
            'file_naming_scheme': ('The [red]naming-pattern[/red] after which files are created; use format: [green]%([bold yellow]option1[/bold yellow])s[/green][red]-[/red][green]%([bold yellow]option2[/bold yellow])s[/green][red]-[/red][green]%([bold yellow]option3[/bold yellow])s[/green].', "[yellow]title[/yellow], [yellow]id[/yellow], [yellow]ext[/yellow], [yellow]uploader[/yellow], [yellow]upload_date[/yellow], [yellow]channel[/yellow], [yellow]channel_id[/yellow], [yellow]view_count[/yellow], [yellow]like_count[/yellow], [yellow]duration[/yellow], [yellow]playlist[/yellow], [yellow]playlist_index[/yellow], [yellow]playlist_id[/yellow]"),
            'open_folder_after_download': ('Open the [red]target directory[/red] after download is [red]done[/red].', "[green]yes[/green] or [red]no[/red]"),
            'use_original_thumbnail': ('Use [red]original thumbnail[/red].', "[green]yes[/green] or [red]no[/red]"),
        },
        'aliases': {
            'audio_download_alias': ('Alias for [red]donwloading audio[/red] only.', '[green]Any Word[/green] should work, avoid spaces or special characters'),
            'video_download_alias': ('Alias for [red]downloading video[/red].', '[green]Any Word[/green] should work, avoid spaces or special characters'),
            'audio_open_alias': ("Alias for [red]navigating[/red] to the [red]Audio-path[/red].", "[green]Any Word[/green] should work, avoid spaces or special characters"),
            'video_open_alias': ('Alias for [red]navigating[/red] to the [red]Video-path[/red].','[green]Any Word[/green] should work, avoid spaces or special characters'),
            'settings_open_alias': ('Alias for [red]navigating[/red] to the [red]Settings-path[/red].', '[green]Any Word[/green] should work, avoid spaces or special characters'),
        },
        'other': {
            'loading_animation': ('[red]Loading animation[/red] style ', '[#A0A0A0]To preview different animations run [/#A0A0A0]: [yellow]python[/yellow] -m [green]rich.spinner[/green] '),
        }
    }

    if section in descriptions and key in descriptions[section]:
        return descriptions[section][key]
    else:
        return '', ''  
if __name__ == "__main__":
    main()
