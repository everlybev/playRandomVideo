import os
import time
import shutil
from os.path import exists
import secrets
from moviepy.editor import VideoFileClip

#cd C:\Users\dudeo\AppData\Local\Programs\Python\Python39
#pyinstaller --onefile hentai_mover.pyw

hentai_destination = 'D:\\Videos\\Petto\\H\\new\\' # this is the directory where hentai ends up
hentai_location_after_watching = 'D:\\Videos\\Petto\\H\\old\\'
root_porn_directory = 'D:\\Videos\\Petto\\'

def get_item_type(item):
    item = str(item)
    item = item.lower()
    if item.endswith('.avi'):
        return 'video'
    elif item.endswith('.mp4'):
        return 'video'
    elif item.endswith('.mpeg'):
        return 'video'
    elif item.endswith('.mov'):
        return 'video'
    elif item.endswith('.mpg'):
        return 'video'
    elif item.endswith('.zip'):
        return 'exit'
    elif item.endswith('.rar'):
        return 'exit'
    elif item.endswith('.ini'):
        return 'exit'
    elif item.endswith('.txt'):
        return 'exit'
    elif item.__contains__('.'):
        return 'exit'
    elif item.__contains__('the bois'):
        return 'exit'
    elif item.__contains__('nihon'):
        return 'exit'
    else:
        return 'folder'

def generate_random_number(folder):
    max_number = len(os.listdir(folder)) - 1
    min_number = 0
    secretsGenerator = secrets.SystemRandom()
    random_number = secretsGenerator.randint(min_number, max_number)
    print(random_number)
    return random_number

def remove_crap(name_of_file):
    name_of_file = name_of_file.replace('-1080p-v1x', '')
    name_of_file = name_of_file.replace('-1080p-v2x', '')
    name_of_file = name_of_file.replace('-720p-v1x', '')
    name_of_file = name_of_file.replace('-720p-v2x', '')
    name_of_file = name_of_file.replace('1080p-v1x', '')
    name_of_file = name_of_file.replace('1080p-v2x', '')
    name_of_file = name_of_file.replace('720p-v1x', '')
    name_of_file = name_of_file.replace('720p-v2x', '')
    name_of_file = name_of_file.replace('-v1x', '')
    name_of_file = name_of_file.replace('-v2x', '')
    name_of_file = name_of_file.replace('v1x', '')
    name_of_file = name_of_file.replace('v2x', '')
    name_of_file = name_of_file.replace('-1080p', '')
    name_of_file = name_of_file.replace('1080p', '')
    name_of_file = name_of_file.replace('-720p', '')
    name_of_file = name_of_file.replace('720p', '')
    name_of_file = name_of_file.replace('-1080', '')
    name_of_file = name_of_file.replace('1080', '')
    name_of_file = name_of_file.replace('-720', '')
    name_of_file = name_of_file.replace('720', '')
    name_of_file = name_of_file.replace('.mp4', '')
    name_of_file = name_of_file.replace('.MP4', '')
    name_of_file = name_of_file.replace('.MPEG', '')
    name_of_file = name_of_file.replace('.mpeg', '')
    name_of_file = name_of_file.replace('.AVI', '')
    name_of_file = name_of_file.replace('.avi', '')
    name_of_file = name_of_file.replace('vx', '')
    return name_of_file

def remove_numbers(name_of_the_file):
    name_of_the_file = name_of_the_file.replace('0', '')
    name_of_the_file = name_of_the_file.replace('1', '')
    name_of_the_file = name_of_the_file.replace('2', '')
    name_of_the_file = name_of_the_file.replace('3', '')
    name_of_the_file = name_of_the_file.replace('4', '')
    name_of_the_file = name_of_the_file.replace('6', '')
    name_of_the_file = name_of_the_file.replace('5', '')
    name_of_the_file = name_of_the_file.replace('7', '')
    name_of_the_file = name_of_the_file.replace('8', '')
    name_of_the_file = name_of_the_file.replace('9', '')
    return name_of_the_file
    

def play_video(vid):
    print(vid)
    os.startfile(vid)


def get_file_legnth(a_video): #return float duration in seconds the legnth of a video
    try:
        clip = VideoFileClip(a_video)
        dur = clip.duration
        clip.close()
        return dur
    except:
        print('Thats not a video')
        return 0



def pick_a_video(index):
    list_of_hentai = os.listdir(hentai_destination)
    potential_hentai = list_of_hentai[index]
    hentai = hentai_destination + potential_hentai
    #make last digit(s) integers
    potential_hentai_minus_crap = remove_crap(potential_hentai)
    #check if last digit is an integer
    try:
        episode_number = int(potential_hentai_minus_crap[len(potential_hentai_minus_crap)-1])
        #check if there is an episode before it
        i = 1
        found = 0
        while found < 1:
            potential_earlier_episode_number = episode_number - 1
            lower_index_filename = list_of_hentai[index-i]
            lower_index_filename_minus_crap = remove_crap(lower_index_filename)
            if remove_crap(remove_numbers(remove_crap(lower_index_filename))) == remove_crap(remove_numbers(remove_crap(potential_hentai))):
                episode_number = episode_number - 1
                potential_hentai = list_of_hentai[index - i]
                hentai = hentai_destination + potential_hentai
                i = i + 1
            else: #they are different series and therefor this is the episode to watch
                found = 2
##                print('1 '+remove_crap(remove_numbers(potential_hentai)))
##                print('2 '+remove_crap(remove_numbers(lower_index_filename)))
        play_video(hentai)
##        if episode_number > 1:
##            potential_earlier_episode_number = episode_number - 1
##        else:
##            play_video(hentai)
    except:
        play_video(hentai)
    return hentai_destination, potential_hentai


new_hentai_folder = False

index_of_folder_or_video = generate_random_number(root_porn_directory)
list_of_stuff_in_root = os.listdir(root_porn_directory)
selected_item = list_of_stuff_in_root[index_of_folder_or_video]
print(selected_item)

if selected_item.__contains__('.ini') or selected_item.__contains__('.txt'):
    print('ini')
    try:
        if index_of_folder_or_video == 0:
            index_of_folder_or_video = index_of_folder_or_video + 1
            selected_item = list_of_stuff_in_root[index_of_folder_or_video]
        else:
            index_of_folder_or_video = index_of_folder_or_video - 1
            selected_item = list_of_stuff_in_root[index_of_folder_or_video]
    except:
        index_of_folder_or_video = index_of_folder_or_video - 1
        selected_item = list_of_stuff_in_root[index_of_folder_or_video]
elif get_item_type(selected_item) == 'exit':
    print('exit')
    try:
        index_of_folder_or_video = index_of_folder_or_video + 1
        selected_item = list_of_stuff_in_root[index_of_folder_or_video]
    except:
        index_of_folder_or_video = index_of_folder_or_video - 1
        selected_item = list_of_stuff_in_root[index_of_folder_or_video]
else:
    print('passed')

print(index_of_folder_or_video)
print(list_of_stuff_in_root)
print(selected_item)
type_of_item = get_item_type(selected_item)
if type_of_item == 'video':
    video = root_porn_directory + selected_item
    print(video)
    play_video(video)
elif type_of_item == 'exit':
    exit(0)
else:
    current_folder = root_porn_directory
    #travel down the folders and find a video
    while type_of_item == 'folder':
        current_folder = current_folder + selected_item + '\\'
        print('---')
        print(current_folder)
        print('---')
        index = generate_random_number(current_folder)
        selected_item = os.listdir(current_folder)[index]
        if current_folder == hentai_destination:
            new_hentai_folder = True
        print(selected_item)
        type_of_item = get_item_type(selected_item)
    video = current_folder + selected_item
    if new_hentai_folder:
        hentai_filename = selected_item
        start_time = time.time()
        duration_of_hentai = get_file_legnth(video)
        play_video(video)
        time.sleep(.75*duration_of_hentai)
        try:
            new_video_access_time = os.path.getatime(video)
            time_delta = new_video_access_time - start_time #how long was it watched
            if time_delta >.7*duration_of_hentai: #If watched 70% of hentai
                time.sleep(.3*duration_of_hentai)
                try:
                    seen_it_folder = str(os.path.join(hentai_location_after_watching, hentai_filename))
                    have_yet_to_see_it_folder = str(os.path.join(starting_location, hentai_filename))
                    shutil.move(have_yet_to_see_it_folder, seen_it_folder)
                except Exception as E:
                    print(E)
                    print('file was already moved!')
        except Exception as E:
            print(E)
            print('file was already moved?')
    else:
        play_video(video)

##starting_location, hentai_filename = pick_a_video(generate_random_number(hentai_destination))
##duration_of_hentai = get_file_legnth(starting_location+hentai_filename)
##
##time.sleep(.75*duration_of_hentai) #wait 3 quaters of the duration for the video to be watched
##
##try:
##    new_video_access_time = os.path.getatime(starting_location+hentai_filename)
##    time_delta = new_video_access_time - start_time #how long was it watched
##    if time_delta >.7*duration_of_hentai: #If watched 70% of hentai
##        time.sleep(.3*duration_of_hentai)
##        try:
##            seen_it_folder = str(os.path.join(hentai_location_after_watching, hentai_filename))
##            have_yet_to_see_it_folder = str(os.path.join(starting_location, hentai_filename))
##            shutil.move(have_yet_to_see_it_folder, seen_it_folder)
##        except Exception as E:
##            print(E)
##            print('file was already moved!')
##except Exception as E:
##    print(E)
##    print('file was already moved?')
###pick_a_video(402)



    
