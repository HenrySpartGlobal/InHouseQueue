## Hosting
Please see my Hosting Readme - https://github.com/HenrySpartGlobal/InHouseQueue/blob/main/docs/HOSTING.md 

# How does it work?
When a match is initiated, 5 buttons appear that represent a role. Once each position has 2 players, all participating players are tagged to announce that a game has been found. All games are given an ID which can be used for various things.

![](https://github.com/HenrySpartGlobal/InHouseQueue/blob/main/assets/match%20start.png)

Players are required to ready up. The queue will have a minimum time to ready up. This is displayed as a time in everyone's **local timezone**, any player who does not ready up is kicked from the queue. Readied-up players will remain in the queue. 
 
Once all players are ready teams are split (no matchmaking yet!) and the match is started. A lobby text channel (suffixed with the `gameId`), 2 Spectator buttons, 2 voice channels (suffixed with the `gameId`) and one voice for each team are created by the bot. These are all private and can only be interacted with by participating players or spectators. Otherwise, it is public for the rest of the server to view.

The spectator buttons enable everyone else to join the voice or Blue or Red team. Players can then decide to stream their match on the discord voice channel for the spectators. 

![](https://github.com/HenrySpartGlobal/InHouseQueue/blob/main/assets/ready%20up.png)

Players are responsible for organising the custom game between themselves.

Once a game has been completed - players can mark the game as won with the `!won command`. This starts a vote, which has `Red Team` or `Blue Team` options, in which 6 votes are required for the win to be counted and tracked to the database. 

![](https://github.com/HenrySpartGlobal/InHouseQueue/blob/main/assets/lobby.png)

Players' wins are tracked and can be displayed with the `!leaderboard` command. An admin command is available if there is any cheating to override false scoring. In an ideal scenario, 5 people on the winning team vote "X team won" and then one more person from the losing team does the same. 

![](https://github.com/HenrySpartGlobal/InHouseQueue/blob/main/assets/leaderboard.png)

Don't worry! The lobby text channel and the team voice channels are deleted once a game is concluded, the roles are also deleted. Further, the results of a game will be sent to a channel of your choice - set this with `/setwinnerlog`. You may have multiple games running on your server at the same time as each game is given a unique ID. This unique ID can be used by admins to cancel, score and reset games. See [Admin](https://github.com/HenrySpartGlobal/InHouseQueue#admin-commands) commands sectin above.  

![](https://github.com/HenrySpartGlobal/InHouseQueue/blob/main/assets/finish.png)
