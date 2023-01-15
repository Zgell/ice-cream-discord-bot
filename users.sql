-- Sets up the "Users" database with all tables needed to run the bot.

-- Create a table of all Discord users who interact with the bot
CREATE TABLE userPerms (
    userid int,         -- The Discord ID of the user
    perms int,       -- The permission level of the user (ranges from 1 to 6, 1 being lowest, 6 being highest)
);