# FSort
#A simple Python script for sorting and clearing files
import os
import shutil

# Add the location for moving each extenson---
dir_lookup = {
    'py': r'.\sorted_file\py',
    'pdf': r'.\sorted_file\pdfs',
    'zip': r'.\sorted_file\compressed_files',
    'rar': r'.\sorted_file\compressed_files',
    'doc': r'.\sorted_file\doc_files',
    'docx': r'.\sorted_file\doc_files',
    'ppt': r'.\sorted_file\presentation_files',
    'pptx': r'.\sorted_file\presentation_files',
    'jpg': r'.\sorted_file\images',
    'jpeg': r'.\sorted_file\images',
    'png': r'.\sorted_file\images',
    'exe': r'.\sorted_file\installation_files',
    'msi': r'.\sorted_file\installation_files',
    'txt': r'.\sorted_file\text_files',
    'mp3': r'.\sorted_file\music',
    'mp4': r'.\sorted_file\video',
    'mkv': r'.\sorted_file\video',
    'rmskin': r'.\sorted_file\rainmeter_skin',
    'iso': r'.\sorted_file\isoAndImages',
    'img': r'.\sorted_file\isoAndImages',
    'csv': r'.\sorted_file\data_files',
    'json': r'.\sorted_file\data_files',
    'xlsx': r'.\sorted_file\excel_files',
    'apk': r'.\sorted_file\android_apps_apk',
    'srt': r'.\sorted_file\subtitle',
}

# add all extensions to be sorted here---
extensions = {
    'pdf','txt', 'exe','doc','docx','ppt','pptx','jpeg','jpg','zip','png','rar','mp3','mp4', 'mkv','msi','rmskin','iso','img','csv','json','xlsx','apk','srt'
}


def list_files2(source_directory, extension, destination_directory):
    if(destination_directory == None):
      return
    for (dirpath, dirnames, filenames) in os.walk(source_directory):
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
        for f in filenames: 
          if f.lower().endswith('.' + extension.lower()):
            shutil.move(source_directory+'\\'+f, destination_directory+'\\'+f)
        return (f for f in filenames if f.lower().endswith('.' + extension))


for e in extensions:

    for f in list_files2('.\\', e, dir_lookup[e]):
        print('sorted file: '+f)

    # print('==============================================')

