WEBPAGE_FILE_FOLDERS=webpages_files

mkdir -p $WEBPAGE_FILE_FOLDERS
cd $WEBPAGE_FILE_FOLDERS
wget -p -k -F --user-agent 'Chrome/79' "https://www.hellenicbank.com/"
