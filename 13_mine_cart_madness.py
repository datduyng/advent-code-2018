large = r"""
  /----------------------------------\                           /---------------------------------------\                                            
  |                                  |   /-----------------------+---------------------------------------+------------------------------------\       
  |      /---------------------------+---+-------------------\   |                 /---------------------+-------------------------------\    |       
  |      |         /---------\     /-+---+-------------------+--\|                 |                     |                               |    |       
/-+------+---------+---------+-----+-+---+------------------>+--++--\              |                     |                   /----------\|    |       
| |      |     /---+-------<-+-----+-+---+-------------------+--++--+--------------+---------------------+--------\          |          ||    |       
| |      |     |   |         |     | |   |                   |  ||  |              |   /-----------------+--------+--------\ |          ||    |       
| |      |     |   |         |     | |   |    /--------------+--++--+--------------+---+-----------------+--------+--------+-+----------++----+--\    
| |      |     |/--+---------+-----+-+---+-\  |        /-----+--++\ |              |   |                 |        |        | |          ||    |  |    
| |      |     ||  |         |    /+-+---+-+--+-<------+-----+--+++-+--------------+---+-----------------+--------+--------+-+------\   ||    |  |    
| | /----+---\ ||  |         |    || |   | |/-+--------+--\  |  ||| |     /--------+---+-----------------+--------+--------+-+------+--\||    |  |    
| | |    |   | ||  |         |    ||/+---+-++-+----\   |  |  |/-+++-+-----+--------+---+-----------------+--------+--------+-+------+-\|||    |  |    
| |/+----+---+-++--+---------+----++++---+-++-+----+---+--+--++-+++-+-----+\       |   |               /-+--------+----\   | |      | ||||    |  |    
| |||    |   | ||  |         |    ||||   | || |    |   |  |  || ||| |     ||       \---+---------------+-+--------+----+---+-+------+-+++/    |  |    
| |||    |   | ||  |         |    ||||   | || |    |  /+--+--++-+++-+-----++-----------+---------------+-+--------+----+---+-+------+-+++-----+--+---\
| |||    |   | ||  |         |    |\++---+-++-+----+--++--+--++-/|| |     ||           |               | |        |    |   | |      | |||     |  |   |
| |||   /+---+-++--+---------+----+-++---+-++-+----+--++-\|  ||  || |     ||           |               | |        |    |   | |      | |||     |  |   |
| |||   ||   | ||  |         |   /+-++---+\|| |  /-+--++-++--++--++-+-----++-----------+---------------+-+--------+----+---+-+-----\| |||     |  |   |
|/+++---++---+-++--+---------+---++-++---++++-+--+-+--++-++--++--++-+-----++-----------+--------\      | |        | /--+---+-+-----++-+++---\ |  |   |
|||||   ||   | \+--+---------+---++-++---++++-+--+-+--++-++--++--++-+-----++-----------+--------+------+-+--------/ |  |   | |     || |||   | |  |   |
|||||   ||   |  |  |         |   || ||   |||| |  | |  || ||  ||  || |     ||      /----+--------+------+-+----------+--+---+-+-----++-+++---+\|  |   |
|||\+---++---+--+--+---------+---++-++---++++-+--+-+--++-++--++--++-+-----+/      |    |/-------+------+-+--\       |  |   | |     || |||   |||  |   |
||| |   ||   |  |  |         |   || ||   |||| |  | |  || ||  ||  || |     |       |/---++-------+------+-+--+--\    |  |   | \-----++-++/   |||  |   |
||\-+---++---+--+--+---------+---++-+/   |||| |  | |  || ||  ||  || |     |       ||   ||       |      | |  |  |    |  |   | /-----++-++----+++--+\  |
||  |   || /-+--+--+---------+---++-+----++++-+--+-+--++-++--++\ || |     |       ||   ||       |      | |  |  |    |  |   | |     || ||    |||  ||  |
||  |   || | | /+--+---------+---++-+----++++-+--+-+--++-++--+++-++-+-----+-------++---++-------+---\  |/+--+--+----+--+---+-+---\ || ||    |||  ||  |
||  |/--++-+-+-++--+-----<---+---++-+----++++-+--+-+--++-++--+++-++-+-----+-------++---++-------+---+--+++\ |  |    |  |   | |   | || ||    |||  ||  |
||  ||  || | | v|  |         |   || |    |||| |  | |  || ||  ||| || |     |       ||   ||       |   |  |||| |  |    |  |   | |   | || ||    |||  ||  |
||  ||  || | | ||  |         |/--++-+----++++-+--+-+--++-++--+++-++-+-----+\      ||   ||       |   |  |||| |  |   /+--+---+-+---+-++\||    |||  ||  |
||  \+--++-+-/ ||  |         ||  || |    |||| |  | |  || ||  ||| || |     ||      ||   ||       |   |  |||| |  |   ||  |   | |   | |||||    |||  ||  |
||   |  || |   ||  |         ||  || |    |||| |  | |  || ||  ||| || |     ||      ||   ||       |   |  \+++-+--+---++--/   | |   | |||||    |||  ||  |
||   |  || |   ||  |         ||  || |    |||| |  | |  || ||  ||| || |     ||      ||   ||       |  /+---+++-+--+---++---\  | |   | |||||    |||  ||  |
||   |  || |   ||  \---------/|  || |    |||| |  | |  || ||  ||| || |     ||  /---++---++-------+--++---+++-+--+--\||   |  | |   | |||||    |||  ||  |
||   |  || |   ||       />----+--++-+----++++-+--+-+-\|| ||  |\+-++-+-----++--+---++---++-------+--++---+++-+--+--+++---+--+-+---+-+++/|    |||  ||  |
||   |  || |   ||       |     |  || |    |||| |  | | ||| ||  | | || |     ||  |   ||   ||  /----+--++---+++-+--+--+++---+--+-+---+-+++\|    |||  ||  |
||   |  || |   ||       |     |  || |    |||| |  | | ||| || /+-+-++-+-----++--+---++---++--+----+--++---+++-+--+--+++---+\ | |   | |||||    |||  ||  |
||   |/-++-+---++-------+-----+--++-+----++++-+--+-+-+++-++-++-+-++-+-----++--+--\||  /++--+----+--++---+++-+--+--+++---++-+-+---+-+++++---\|||  ||  |
||   || || |   ||       |     |  || |    |||| |  | | ||| || || | || |     ||  |  |||  |||  | /--+--++---+++-+--+--+++---++-+-+---+-+++++---++++-\||  |
||   || || |   ||       |     |  |\-+----++++-+--+-+-+++-++-++-+-++-+-----++--+--+++--+++--+-+--+--++---+++-+--+--+++---++-+-+---+-+/|||   |||| |||  |
||   || || |   || /-----+-----+--+--+----++++-+--+-+-+++-++-++-+-++-+-----++--+--+++--+++--+-+-\|  ||   ||| |  |  |||   || | |   | | |||   |||| |||  |
||   || || | /-++-+-----+-----+\ |  |   /++++-+--+-+-+++-++-++-+-++-+-----++--+--+++--+++--+-+-++--++---+++-+-\|  |||   || | |   | | |||   |||| |||  |
||   || || | |/++-+-----+-----++-+--+---+++++-+--+-+-+++-++-++-+-++-+-----++--+--+++\ |||  | | ||  ||   ||| | ||  |||   || | |   | | |||   |||| |||  |
|\---++-++-+-++++-+-----+-----++-+--+---+++++-+--+-+-+++-++-++-+-++-+-----++--+--++++-+++--+-+-+/  ||   ||| | ||  |||   || | |   | | |||   |||| |||  |
|    || || | |||| |     |     || |  |   ||||| |  | | ||| || || | || |     ||  | /++++-+++--+-+-+---++---+++-+-++--+++---++-+-+---+-+-+++-\ |||| |||  |
|   /++-++-+-++++-+\    |     || |  |   |||||/+--+-+-+++-++-++-+-++-+-----++--+-+++++-+++--+-+-+---++\  ||| | ||  |||   || | |   | | ||| | |||| |||  |
|   ||| || | |||| ||    |     || |  |   |||||||  | | ||| || || | || |     ||  | ||||| |||  | | |   |||  ||| | ||  |||   || | |   | | ||| | |||| |||  |
|   ||| || | |||| ||    |     || |  \---+++++++--+-/ ||| || || | || |     ||  \-+++++-+++--+-+-+---+++--+++-+-++--/||   || | |   | | ||| | |||| |||  |
|   ||| || | |||| ||/---+-----++-+------+++++++--+---+++-++-++-+-++-+-----++\   ||||| |||  | | |   |||  ||| | ||   ||   || | |   | | ||| | |||| |||  |
|   ||| v| | |||| |||   |     || |      |||||||  |   ||| || || | || |     |||   ||||| |||  | | |   |||  ||| | ||   ||   || | |   | | ||| | |||| |||  |
|   ||| || | |||| |||   |     || |      |||||||  |   ||| || || | || |     |||   ||||| |||  | \-+---+++--+++-+-++---++---++-+-+---+-+-+++-+-++++-/||  |
|   ||| || | |||| ||| /-+-----++-+------+++++++--+---+++-++-++-+-++-+----\|||   ||||| |||  v   |   |||  ||| | ||   ||   || | |   | | ||| | ||||  ||  |
|   ||| || | |||| |||/+-+-----++-+---\  |||||||  |   ||| || || | || |    ||||   ||||| |||  |   |   |||  ||| | ||   ||   || | | /-+-+-+++-+-++++-\||  |
|   ||| || | |||| |||||/+-----++-+---+--+++++++--+---+++-++-++-+-++-+----++++---+++++-+++--+---+---+++--+++-+-++---++---++\| | |/+-+-+++-+-++++-+++\ |
|   ||| || | |||| |||||||     || |   |  |||||||  |   ||| || || | || | /--++++---+++++-+++--+---+-\ |||  \++-+-++---++---++++-+-++/ | ||| | |||| |||| |
|   ||| || | |||| |||||||   /-++-+---+--+++++++--+---+++-++-++-+-++-+-+--++++---+++++-+++--+---+-+-+++---++-+-++---++---++++-+-++-\| ||| | |||| |||| |
|   ||| || | |||| |||||||   | || |   |  |||||||  |   ||\-++-++-+-+/ | |  ||||   |||\+-+++--+---+-+-+++---++-+-+/   ||   |||| | || || ||| | |||| |||| |
|   ||| || | |||| |||||||   | || |   |  |||||||  |   ||  || || | \--+-+--++++---+++-+-+++--+---+-+-+++---/| | |    ||   |||| | || || ||| | |||| |||| |
|   ||| || | |||| |||||||   | || |   |  |||||||  |   ||  || || |    | |  ||||   ||\-+-+++--+---+-+-+++----+-+-+----++---++++-+-++-++-+++-+-++/| |||| |
|   ||| || | |||| |||||||   | || |   |  |||||||  | /-++--++-++-+----+-+--++++---++--+-+++-<+---+-+-+++----+-+-+----++---++++-+-++-++\||| | || | |||| |
|   ||| || | |||| |||||||   | || |   |  |||||||  | | ||  || || |    | |  ||||   ||  | |||  | /-+-+-+++----+-+\|    ||   |||| | || |||||| | || | |||| |
|   ||| || | |||| |||||||   | || |   |  |||||||  | | ||  || || |    | |  ||||   ||  | \++--+-+-+-+-+++----+-+++----++---++++-+-++-++++++-+-/| | |||| |
\---+++-++-+-++++-+++++++---+-++-+---+--+++++++--+-+-++--++-++-+----/ |  ||||   ||  |  ||  | | | | |||    | |||    ||   |||| | || |||||| |  | | |||| |
    ||| || | |||| |||||||   |/++-+---+--+++++++-\| | ||  || \+-+------+--++++---++--+--++--+-+-+-+-+++----+-+++----++---+/|| | || |||||| |  | | |||| |
    ||| || | |||| |||||||   |||| |   |  ||||||| || | ||  ||  | |      |  ||||   ||  |  ||  | | | | |||    | |||    ||   | || | || |||||| |  | | |||| |
    ||| || | |||| |||||||   \+++-+---+--+++++++-++-+-++--++--+-+------+--++++---++--+--++--+-+-+-+-+++----+-+++----++---+-++-+-++-/||||| |  | | |||| |
    ||| || | |||| \++++++----+++-+---+--+++++++-++-+-++--++--+-+------+--++++---++--+--++--+-+-/ | |||    | |||    ||   | || | ||  ||||| |  | | |||| |
    ||| || | ||||  ||||||    ||| |   |  |\+++++-++-+-++--++--+-+------+--++++---++--+--++--+-+---+-+++----+-+++----++---+-++-+-++--+++++-+--+-/ |||| |
    ||| || | ||||/-++++++----+++-+---+--+-+++++-++-+-++--++--+-+------+--++++---++--+--++-\| |   | |||    | |||    ||   | || | ||  ||||| |  |   |||| |
    ||| || | ||||| ||||||    ||| |   |  | ||||| || \-++--++--+-+------+--++++---++--+--++-++-+---+-+++----+-+++----++---+-++-+-++--+/||| |  |   |||| |
    \++-++-+-+++++-/|||||    ||| |   |  | ||||| ||   ||  ||  |/+------+--++++---++--+--++-++-+---+-+++----+-+++----++---+-++-+-++-\|/+++-+--+\  |||| |
     || || | |||||  |||||    ||| |   |  | ||||| ||   ||  ||  |||      |  ||||   \+--+--++-++-+---+-+++----+-+++----++---+-++-+-++-++++++-/  ||  |||| |
     || || | ||\++--+++++----+++-+---+--+-+++++-++---++--++--+++------+--++++----+--+--++-++-+---+-+/|    | |||    ||   | || | || ||||||    ||  |||| |
     || || | || ||  |||||    ||| |   |  | ||||| ||   ||  ||  |||    /-+--++++----+--+--++-++-+\  | | |    | |||    ||   | || | || ||||||    ||  |||| |
     || || | || ||  |||\+----+++-+---+--+-+++++-++---++--++--+++----+-+--++++----+--+--++-++-++--+-+-+----+-+++----++---+-/| | || ||||||    ||  |||| |
     || || | || ||  ||| |    ||| |   |  | ||||| ||   ||  || /+++----+-+--++++----+--+-\|| || ||  | | |    ^ |||    ||   |  | | || ||||||    ||  |||| |
    /++-++-+-++-++--+++-+----+++\\---+--+-/|||| ||   ||  || ||||    | |  ||||    |  | ||| || \+--+-+-+----+-+/|    ||   |  | | || ||||||    ||  |||| |
  /-+++-++-+-++-++--+++-+----++++----+--+--++++-++---++--++-++++----+-+--++++----+--+-+++-++--+--+-+-+----+\| |    ||   |  | | || ||||||    ||  |||| |
  | ||| || | || ||  ||| |    ||||/---+--+--++++-++---++--++-++++----+-+--++++----+--+-+++-++--+--+-+-+-\  ||| |    ||   |  | | || ||||||    ||  |||| |
  | ||| || | || ||  ||| |    |||||  /+--+--++++-++---++-\|| ||||    | |  ||||    | /+-+++-++--+--+-+-+-+--+++-+----++---+--+-+-++-++++++\   ||  |||| |
  | ||| || | || || /+++-+----+++++--++--+--++++-++---++-+++-++++----+-+--++++----+-++-+++-++--+--+-+-+-+--+++\|    ||   |  | | || |||||||   ||  |||| |
  | ||| |\-+-++-++-++++-+----+++++--++--+--++++-++---++-+++-+/||    | |  ||||    | || ||| ||  |  | | | |  |||||    ||   |  | | \+-+++++++---++--/||| |
  | ||| |  | || || |||| |    |||||  ||  |  |||| ||   || ||| | ||    | |  ||||    | || ||| ||  |  | | | |  |||||    ||   |  | |  | |||||||   ||   ||| |
  | ||| |  | || || |||| |    |||||  ||  |  |||| |\---++-+++-+-++----+-+--++++----+-++-+++-++--+--+-+-+-+--+++++----++---+--+-+--+-+/|||||   ||   ||| |
  | ||| |  | || || |||| |    |||||  ||  |/-++++-+----++-+++-+-++----+-+--++++----+-++-+++-++--+--+-+-+-+--+++++----++---+--+-+--+-+-+++++-\ ||   ||| |
  | ||| |  | || ||/++++-+--\ |||||  ||  || |||| |    || |||/+-++----+-+--++++----+-++-+++-++--+--+-+-+\|  |||||    ||   |  | |  | | ||||| | ||   ||| |
 /+-+++-+--+-++-+++++++-+--+-+++++--++--++-++++-+----++-+++++-++----+-+--++++--\ | || ||| ||  |  | | |||  |||||    ||   |  | |  | | ||||| | ||   ||| |
 || ||| |  | || ||||||| |  | |||||  ||  || |||| |    || ||||| ||    | |/-++++--+-+-++-+++\||  |  | | |||  |||||    ||   |  | |  | | ||||| | ||   ||| |
 || ||| |  | || ||||||| |  | |||||  ||  || |||| |    || ||||| ||    | || ||||  | | || ||||||  |  | | |||  |||||    ||   |  | |  | | ||||| | ||   ||| |
 || |\+-+--+-++-+++++++-+--+-+++++--++--++-++++-+----++-+++++-++----+-++-++++--+-+-++-++++++--+--+-+-+++--/||||    ||   |  | |  | | ||||| | ||   ||| |
 || | | |  | || |||\+++-+--+-+++++--++--++-++++-+----++-+++++-++----+-++-++++--+-+-++-++++++--+--+-+-+++---++/|    ||   |  | |  | | ||||| | ||   ||| |
 || | | |  | ||/+++-+++-+--+-+++++--++--++-++++-+--\ || ||||| ||    \-++-++++--+-+-++-++++++--/  | | |||   || |    ||   |  | |  | | ||||| | ||   ||| |
 || | | |  | |||||| ||\-+--+-+++++--++--++-++++-+--+-++-+++++-++------++-/|||  | | || ||||||     | | |||   || |    ||   |  | |  | | ||||| | ||   ||| |
 || | | |  | ||||||/++--+--+-+++++--++--++-++++-+--+-++-+++++-++------++--+++--+-+-++-++++++-\   |/+-+++---++-+---\||   |  | |  | | ||||| | ||   ||| |
 || | | |  | |||||||||  |  | |||||  ||  || |||| |  | || ||||| ||   /--++--+++--+-+-++\|||||| |   ||| |||   || |   |||   |  | |  | | ||||| | ||   ||| |
 || | | | /+-+++++++++--+-\| |||||  ||  || |||| |  | || ||||| ||   |  ||  |||  | | ||||||||| |   ||| |||   || |   |||   |  | |  | | ||||| | ||   ||| |
 || | | | || ||||||||\--+-++-+++++-<+/  || |||| |  | |\-+++++-++---+--++--+++--+-+-+++++++++-+---+++-+++---++-+---+++---+--+-+--+-+-+++++-+-++---+++-/
 || | | \-++-++++++++---+-++-+++++--+---++-++++-+--+-+--+/||| ||   |  ||  |||  | | ||||||||| |   ||| |||   || |   ||\---+--+-+--+-+-+++++-+-/|   |||  
 || | |   || ||||||||   | || |||||  |   || |||| |  | |  | ||| ||   |  ||  |||  | | ||||||||| | /-+++-+++---++-+---++----+--+-+--+-+\||||| |  |   |||  
 || | |   || ||||||||   | || |||||  |   || |||| |  | |  |/+++-++---+--++--+++--+-+-+++++++++-+-+-+++-+++---++-+---++----+--+-+--+-+++++++-+--+---+++-\
 || | |   || ||||||||   | || ||||| /+---++-++++-+--+-+--+++++-++---+--++--+++--+-+-+++++++++-+-+-+++-+++---++-+---++----+--+-+--+-+++++++-+-\|   ||| |
 || | |   || ||||||||   | || \++++-++---++-++++-/  | |  ||||| ||   |  ||  |||  | v ||||||||| | | ||| |||   || |   ||    |  | \--+-+++++++-+-++---+/| |
 || | |   || ||\+++++---+-++--++++-++---++-++++----/ |  |||||/++---+--++--+++--+-+\||||||||| | | ||| |||   || |   ||    |  |    | ||||||| | ||   | | |
 || | |   || \+-+++++---+-++--+/|| ^|   || ||||      |  ||||\+++---+--++--+++--+-+++++/||||| | | |\+-+++---++-+---/|    |  |    | ||||||| | ||   | | |
 || | |   ||  | |||||   | ||  | || ||   || ||||      |  |||| |||   | /++--+++--+-+++++-+++++-+-+-+-+-+++---++-+----+---\|  |    | ||||||| | ||   | | |
 || | |   ||  | |||||   | ||  | || ||   || ||||      |  v||| |||   | |||  \++--+-+++++-+++++-+-+-+-+-+++---++-+----+---++--+----+-+++++/| | ||   | | |
 || | |   ||  | |||||   | ||  | || ||   || ||||      |  |||| |||   | |||   ||  | ||||| ||||| | | | | |||   || |    \---++--+----+-+++/| | | ||   | | |
 || | |   ||  | |||||  /+-++--+-++-++\  || |||\------+--++++-+++---+-+++---++--+-+++++-+++++-+-+-+-+-+++---++-+--------++--+----+-+++-+-+-+-++---/ | |
 |\-+-+---++--+-+++++--++-++--+-++-+++--++-+++-------+--++++-+++---+-+++---++--+-+++++-+++++-+-+-+-+-+++---/| |        ||  |    | ||| | | | ||     | |
 |  | |   ||  | \++++--++-++--+-++-+++--++-/||       |  |||| |||   | |||   ||  | ||||| |\+++-+-+-+-+-+++----/ |        ||  |    | ||| | | | ||     | |
 |  | |   ||  |  ||||  || ||/-+-++-+++--++--++-------+--++++-+++---+-+++---++--+-+++++-+-+++-+-+-+-+-+++------+--------++--+----+-+++-+\| | ||     | |
 |  | |   ||  |  ||||  || ||| | || |||  \+--++-------+--++++-+++---+-+++---++--+-+++++-+-+++-+-+-+-+-+++------/        ||  |    | ||| ||| | ||     | |
 |  | |   ||  \--++++--++-+++-+-++-+++---+--++-------+--++++-+++---+-+++---++--+-+++/| \-+++-+-+-+-+-+++---------------++--/    | ||| ||| | ||     | |
 |  | |   ||     |||\--++-+++-+-++-+++---+--++-------+--++++-+++---+-+++---+/  | ||| |   ||| | | | | |||    /----------++-------+-+++\||| | ||     | |
 |  | |   ||     |||   || ||| | || |||   |  ||       |  |||| |||   | |||   |   | ||| |   ||| | | | | |||    |          ||       | ||\++++-+-+/     | |
 |  | |   ||     |||   || ||| | || |||   |  ||/------+--++++-+++-<-+-+++---+---+-+++-+---+++-+-+-+-+-+++----+----------++-------+-++-++++-+-+--\   | |
 \--+-+---++-----+++---++-+++-+-++-+++---+--+++------+--++++-+++---+-+++---+---/ ||\-+---+++-+-+-+-+-+++----+----------++-------+-++-+++/ | |  |   | |
    | |   ||     |||   || ||| | || |||   |  |||      |  |||| |||   | |||   |     ||  |   ||| | | | | |||    |          ||       \-++-+++--+-+--+---/ |
    | |   ||     |||   || ||| | || |||   |  \++------+--++/| |||  /+-+++---+-----++--+\  ||| | \-+-+-+++----+----------++---------+/ |||  | |  |     |
/---+-+---++-----+++---++\||| | || |\+---+---++------+--/| | |||  || |||   |   /-++--++--+++-+---+-+-+++----+----------++---------+--+++--+-+\ |     |
|   | |   ||     |||   |||v|| |/++-+-+---+---++------+---+-+-+++--++-+++---+---+-++--++--+++-+-\ | | |||    |         /++---------+--+++-\| || |     |
|   \-+---++-----+++---++++++-++/| | |   |   ||      |   | | |||  || |||   |   | ||  ||  ||| | | | | |||    |         |||         |  ||| || || |     |
|     |   ||     |||   |||||| || |/+-+---+---++----\ |   | | |||  || \++---+---+-++--++--+++-+-+-+-+-+++----+---------+/|         |  ||| || || |     |
|     |   ||     |||   |||||| || ||| |  /+---++----+-+---+-+-+++--++--++---+---+-++--++--+++-+-+-+\| |||    |         | |         |  ||| || || |     |
|     |   ||     |||   |||||| || ||| |  ||   ||    | |   | \-+++--++--++---+---+-++--++--+++-+-+-+++-+/|    |         | |         |  ||| || || |     |
|     |   ||     |||   |||||| || \++-+--++---++----+-+---+---+++--++--++---+---+-++--++--+++-+-+-+++-+-/    |         | |         |  ||| || || |     |
|     |   \+-----+++---+++/|| ||  || |  ||   ||    | |   |   \++--++--++---+---+-+/  ||  ||| | | ||| |      |         | |         |  ||| || || |     |
|     |    |     |||   ||| || ||  || |  ||   ||    | |   |    ||  ||  ||   |   | |   ||  ||| | | ||\-+------+---------+-/         |  ||| || || |     |
|     |    \-----+++---+++-++-++--++-+--++---++----+-+---+----+/  ||  ||   |   | |   ||  ||| | | ||  |      |         |           |  ||| || || |     |
|     \----------+++---+++-++-++--++-+--++---++----+-+---+----+---++--++---+---+-/   ||  ||\-+-+-++--+------+---------+-----------+--+/| || || |     |
|                |||   ||| || ||  || |  ||   ||    | |   |    |   ||  ||   |   |     ||  ||  | | ||  |      \---------+-----------+--/ | || || v     |
|                |||   ||| || \+--++-+--++---++----+-+---+----+---++--++---/   |     ||  ||  | | ||  |                \-----------+----+-/| || |     |
|                \++---+++-++--+--++-+--++---++----+-+---+----+---++--++-------+-----++--+/  | | ||  |                            |    |  | || |     |
|                 ||   ||| ||  |  || |  ||   ||    | |   |    |   |\--++-------+-----/|  |   | | ||  |                            |    |  | || |     |
|                 ||   ||| ||  |  \+-+--++---++----/ |   |    |   |   ||       |      |  |   | | ||  |                            |    |  | || |     |
|                 ||   ||| ||  |   | |  ||   ||      |   |    |   |   ||       |      |  |   | | ||  |                            |    |  | || |     |
|                 |\---+++-++--+---+-+--++---++------+---+----+---+---++-------+------+--+---/ | ||  |                            |    |  | || |     |
|                 |    ||| ||  |   | |  \+---++------+---+----+---+---++-------+------+--+-----+-+/  |                            |    |  | || |     |
|                 |    ||| ||  |   | |   |   ||      |   |    |   \---++-------+------/  |     | |   |                            |    |  | || |     |
|                 |    ||| ||  |   | |   |   ||      |   |    |       ||       \---------+-----+-+---+----------------------------+----+--+-+/ |     |
\-----------------+----++/ ||  |   | |   |   ||      |   |    |       |\-----------------/     | |   |                            |    |  | |  |     |
                  |    ||  ||  \---+-+---+---++------+---+----+-------+------------------------/ |   |                            |    |  | |  |     |
                  |    |\--++------+-+---+---++------/   |    |       |                          |   |                            |    |  | |  |     |
                  |    |   |\------+-+---+---++----------+----+-------+--------------------------+---+----------------------------+----/  | |  |     |
                  |    |   |       | |   |   |\----------+----+-------+--------------------------+---+----------------------------+-------+-+--/     |
                  |    |   |       \-+---+---+-----------+----+-------+--------------------------+---+----------------------------+-------+-/        |
                  |    |   |         |   \---+-----------+----+-------+--------------------------+---+----------------------------+-------/          |
                  |    |   |         |       |           |    |       \--------------------------/   |                            |                  |
                  |    \---+---------/       |           \----+--------------------------------------+----------------------------+------------------/
                  |        |                 \----------------+--------------------------------------/                            |                   
                  \--------/                                  \-------------------------------------------------------------------/                   
""".split('\n')


small = r"""
/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   
""".split('\n')

part2 = r"""
/>-<\  
|   |  
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/
""".split('\n')
part2.pop(0)
small.pop(0)
large.pop(0)


class Cart: 
    def setVel(self):
        if(self.facing == 0):#'^'
            self.dx = 0
            self.dy = -1
        elif(self.facing == 1):#'>'
            self.dx = 1
            self.dy = 0
        elif(self.facing == 2):#'v'
            self.dx = 0
            self.dy = 1
        elif(self.facing == 3):#'<'
            self.dx = -1
            self.dy = 0
    def __init__(self, face, x,y):
        self.facing = '^>v<'.index(face)
        self.x = x
        self.y = y 
        self.state = 0
        self.dx = 0 
        self.dy = 0 
        self.setVel()
    def turnLeft(self):
        self.facing = (self.facing-1)%4
    def turnRight(self):
        self.facing = (self.facing+1)%4
    def turn(self):
        if(self.state == 0):
            self.turnLeft()#turn left
        elif(self.state == 2):
            self.turnRight()#turn right
        self.state = (self.state+1)%3
    def move(self, nextTile):
        self.x += self.dx
        self.y += self.dy
        if(nextTile == '\\'):
            if(self.facing == 1): self.turnRight()
            elif(self.facing == 3): self.turnRight()
            elif(self.facing == 0): self.turnLeft()
            elif(self.facing == 2): self.turnLeft()
        elif(nextTile == '/'):
            if(self.facing == 3): self.turnLeft()
            elif(self.facing == 1): self.turnLeft()
            elif(self.facing == 2): self.turnRight()
            elif(self.facing == 0): self.turnRight()
        elif(nextTile == '+'):
            self.turn()#turn with decision 
        #set velocity for next move 
        self.setVel()
    def __str__(self):
        return "(%d,%d) vel(%d,%d) facing:%s State:%d"%(self.x,self.y,self.dx,self.dy, '^>v<'[self.facing],self.state)


def printList(mylist):
    for c in mylist:
        print(c)

'''
if cart have same  coordinate that mean that there is a collision
'''
def isCollision(carts):
    map = {} 
    for index,cart in enumerate(carts):
        if((cart.x,cart.y) not in map):
            map[(cart.x,cart.y)] = 1 
        else:
            return cart
    return None

def updateBoard(file):#file=game board 
    board = []
    carts = []
    for row,line in enumerate(file): 
        for col,c in enumerate(line): 
            if c in '^>v<':
                carts.append(Cart(c,col, row))
        board.append(line.replace('^','|').replace('v','|').replace('>','-').replace('<','-'))

    count=0
    # printList(board)
    # print("start")
    # printList(carts)
    # while(firstCollision(carts) == None):#while there is no collison
    while(len(carts)>1):
        # print('===',count)
        for cart in carts:#update cart coor
            cart.move(board[cart.y+cart.dy][cart.x+cart.dx])
            collision = isCollision(carts)
            if(collision != None):#there might be a collision in here
                print("Stage:",count,"Collision at:",collision)
                return

        # printList(carts)
        count +=1
    print(isCollision(carts))
    print(count)


'''
update until only one cart left
'''
def lastCartPos(file):#file=game board 
    board = []
    carts = []
    for row,line in enumerate(file): 
        for col,c in enumerate(line): 
            if c in '^>v<':
                carts.append(Cart(c,col, row))
        board.append(line.replace('^','|').replace('v','|').replace('>','-').replace('<','-'))

    count=0
    # printList(board)
    # print("start")
    # printList(carts)
    # while(firstCollision(carts) == None):#while there is no collison
    while(len(carts)>1):
        print('===',count)
        for cart in carts:#update cart coor
            cart.move(board[cart.y+cart.dy][cart.x+cart.dx])
            print("before remove")
            printList(carts)
            collision = isCollision(carts)
            if(collision != None):#there might be a collision in here
                for c in carts:
                    if(collision.y == c.y and collision.x == c.x):
                        print("Stage:",count,"Collision at:",collision)
                        carts.remove(c)
                        carts.remove(collision)

        # printList(carts)
        count +=1
    print(isCollision(carts))
    print(count)

updateBoard(large)
print("part2---")
lastCartPos(part2)

'''
My part 1 
firstCollision at (123,18) in my case at state of 230-231 game
17| |||   /+---+-++--+---------+----+-++---+-++-+----+--++-\|  ||  || |     ||           |               | |        |    |   v |      | |||     |  |   |
18| |||   ||   | ||  |         |   /+-++---+\|| |  /-+--++-++--++--++-+-----++-----------+---------------+-+--------+----+--->-+-----\| |||     |  |   |19
19|/+++---++---+-++--+---------+---++-++---++++-+--+-+--++-++--++--++-+-----++-----------+--------\      | |        | /--+---+-+-----++-+++---\ |  |   |
=== 230
(123,17) vel(0,1) facing:v State:0
(134,20) vel(1,0) facing:> State:0
(35,106) vel(0,-1) facing:^ State:1
(9,20) vel(0,1) facing:v State:1
(102,116) vel(0,1) facing:v State:2
(89,43) vel(1,0) facing:> State:1
(116,82) vel(0,-1) facing:^ State:2
(107,64) vel(1,0) facing:> State:2
(61,119) vel(0,-1) facing:^ State:2
(63,41) vel(0,-1) facing:^ State:0
(28,56) vel(0,-1) facing:^ State:1
(110,35) vel(-1,0) facing:< State:0
(47,44) vel(1,0) facing:> State:0
(29,67) vel(0,-1) facing:^ State:0
(125,52) vel(0,1) facing:v State:1
(123,18) vel(1,0) facing:> State:0
(80,142) vel(1,0) facing:> State:1
'''


    