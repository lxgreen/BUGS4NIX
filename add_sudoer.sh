if [ "$1" -ne "/etc/sudoers" ]; then

  # When you run the script, you will run this block since $1 is empty.
  # We first set this script as the EDITOR and then starts visudo.
  # Visudo will now start and use THIS SCRIPT as its editor
  export NEW_SUDOER=$1 && export EDITOR=$0 && sudo -E visudo
else
  # When visudo starts this script, it will provide the name of the sudoers 
  # file as the first parameter and $1 will be non-empty. Because of that, 
  # visudo will run this block.
  # We change the sudoers file and then exit  
  echo $NEW_SUDOER >> $1
fi