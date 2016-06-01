if [ "$1" != "/etc/sudoers" ]; then 
  export NEW_SUDOER=$1 && export EDITOR=$0 && -E visudo
else  
  echo $NEW_SUDOER >> $1
fi