## name of the cli -> share_clip

**HOW IT WORKS**
you start a "session" between devices which will share their clipboard and for ease of my raspberry pi hosted backend if there is only two devices its possible to communicate between each other without much complexity so two devices get peer to peer communication (idk if its called that i am guessing the term) and for more than two devices i am using raspbeery pi 4 backend for synchronixizing the devices
**More than two people communication**
start a room for sharing clipboard -> share_clip --create <name> --notDirect
join a room -> share_clip --join <name> --notDirect

**FUTURE FEATURES**
Able to save "conversations" between clipboards and later access them
