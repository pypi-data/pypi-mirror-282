import os
import subprocess
import platform
import sys

def get_input(prompt):
    return input(prompt).strip()

def get_best_format_code(formats):
    best_format_line = formats[0]
    best_format_code = best_format_line.split()[0]
    return best_format_code

def get_video_formats(link):
    yt_dlp_cmd = f'yt-dlp -F "{link}"'
    result = subprocess.run(yt_dlp_cmd, shell=True, capture_output=True, text=True)
    formats = result.stdout.splitlines()
    return formats

def download_video(link, format_code, start_time, duration, end_time, output_path):
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    if start_time:
        start_time_param = f"-ss {start_time}"
    else:
        start_time_param = ""

    if duration:
        duration_param = f"-t {duration}"
        end_time_param = ""
    elif end_time:
        duration_param = ""
        end_time_param = f"-to {end_time}"
    else:
        duration_param = ""
        end_time_param = ""

    yt_dlp_cmd = f'yt-dlp -f {format_code} -g "{link}"'
    result = subprocess.run(yt_dlp_cmd, shell=True, capture_output=True, text=True)
    video_url = result.stdout.strip()

    ffmpeg_cmd = f'ffmpeg {start_time_param} {duration_param} {end_time_param} -i "{video_url}" -c copy "{output_path}"'
    subprocess.run(ffmpeg_cmd, shell=True)

def main():
    author_info = "Made by Avinion\nTelegram: @akrim"
    print(author_info)
    
    language_prompt = "Choose language / Выберите язык (E/R): "
    language = get_input(language_prompt).upper()

    if language == "E":
        prompts = {
            "link": "Enter the video page link: ",
            "formats": "Available formats:\n{}\nEnter the desired format: ",
            "start_time": "Enter the start time (or press Enter to start from the beginning): ",
            "duration": "Enter the duration (or press Enter to skip): ",
            "end_time": "Enter the end time (or press Enter to download till the end): ",
            "output_file": "Enter the output file name with optional path (e.g., output.mp4 or C:\\path\\to\\output.mp4): ",
            "continue": "Do you want to continue? (y/n): "
        }
    elif language == "R":
        prompts = {
            "link": "Введите ссылку на страницу видео: ",
            "formats": "Доступные форматы:\n{}\nВведите желаемый формат: ",
            "start_time": "Введите время начала (или нажмите Enter, чтобы начать с начала): ",
            "duration": "Введите продолжительность (или нажмите Enter, чтобы пропустить): ",
            "end_time": "Введите время окончания (или нажмите Enter, чтобы скачать до конца): ",
            "output_file": "Введите имя выходного файла с указанием пути (например, output.mp4 или C:\\path\\to\\output.mp4): ",
            "continue": "Хотите продолжить? (y/n): "
        }
    else:
        print("Invalid language choice / Неверный выбор языка")
        sys.exit()

    while True:
        link = get_input(prompts["link"])
        
        formats = get_video_formats(link)
        format_list = "\n".join(formats)
        format_code = get_input(prompts["formats"].format(format_list))

        if not format_code:
            format_code = get_best_format_code(formats)

        start_time = get_input(prompts["start_time"])
        duration = get_input(prompts["duration"])

        end_time = ""
        if not duration:
            end_time = get_input(prompts["end_time"])

        output_path = get_input(prompts["output_file"])

        download_video(link, format_code, start_time, duration, end_time, output_path)

        continue_choice = get_input(prompts["continue"]).lower()
        if continue_choice != 'y':
            break
        os.system('cls' if platform.system() == 'Windows' else 'clear')

if __name__ == "__main__":
    main()
