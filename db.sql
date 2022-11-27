CREATE TABLE `Player` (
  `player_id` int,
  `country_code` int,
  `username` varchar(255),
  `name` varchar(255),
  `money_spent` int,
  `in_game_currency_gems` int,
  `in_game_currency_gold` int,
  `Level` int,
  `Player_location` varchar(255),
  `server_ip` int,
  `Class_name` varchar(255),
  PRIMARY KEY (`player_id`)
);

CREATE TABLE `Player_Achievements` (
  `player_id` int,
  `Achievements` varchar(255),
  PRIMARY KEY (`player_id`, `Achievements`)
);

CREATE TABLE `Boss_Attacks` (
  `Dungeon_name` varchar(255),
  `Boss` varchar(255),
  `attacks` int,
  PRIMARY KEY (`Boss`, `Dungeon_name`, `attacks`)
);

CREATE TABLE `TRADE` (
  `seller_id` int,
  `buyer_id` int,
  PRIMARY KEY (`seller_id`, `buyer_id`)
);

CREATE TABLE `BUY` (
  `Player_id` int,
  `Item_id` int,
  `NPC_name` varchar(255),
  `Location_id` int,
  PRIMARY KEY (`Player_id`, `Item_id`, `NPC_name`, `Location_id`)
);

CREATE TABLE `Class` (
  `Class_name` varchar(255),
  `Class_type` varchar(255),
  PRIMARY KEY (`Class_name`)
);

CREATE TABLE `Class_Weapons` (
  `Class_name` varchar(255),
  `Weapons_used` varchar(255),
  PRIMARY KEY (`Class_name`, `Weapons_used`)
);

CREATE TABLE `Boss` (
  `Dungeon_name` varchar(255),
  `Name` varchar(255),
  `max_health` int,
  `difficulty` int,
  PRIMARY KEY (`Dungeon_name`, `Name`)
);

CREATE TABLE `NPC` (
  `NPC_name` varchar(255),
  `Location_id` int,
  `Type` varchar(255),
  PRIMARY KEY (`NPC_name`, `Location_id`)
);

CREATE TABLE `NPC_Gender` (
  `NPC_name` varchar(255),
  `Gender` varchar(255),
  PRIMARY KEY (`NPC_name`)
);

CREATE TABLE `Dungeon` (
  `Name` varchar(255),
  `min_level_requirement` int,
  `Avg_clear_time` int,
  `max_party_size` int,
  PRIMARY KEY (`Name`)
);

CREATE TABLE `Dungeon_Mob` (
  `Dungeon_Name` varchar(255),
  `Mob_type` varchar(255),
  `Mob_level` int,
  PRIMARY KEY (`Dungeon_Name`, `Mob_type`, `Mob_level`)
);

CREATE TABLE `DROPS` (
  `Dungeon_name` varchar(255),
  `Boss_Name` varchar(255),
  `Item_id` int,
  PRIMARY KEY (`Dungeon_name`, `Boss_Name`, `Item_id`)
);

CREATE TABLE `OWNED_BY` (
  `Item_ID` int,
  `Player_id` int,
  PRIMARY KEY (`Item_ID`, `Player_id`)
);

CREATE TABLE `SERVER` (
  `IP` varchar(255),
  `Server_location` varchar(255),
  `Player_count` int,
  `Traffic` int,
  PRIMARY KEY (`IP`)
);

CREATE TABLE `Location` (
  `Location_id` int,
  `location_name` varchar(255),
  `Terrain` varchar(255),
  `zone_type` varchar(255),
  PRIMARY KEY (`Location_id`)
);

CREATE TABLE `Item` (
  `Item_ID` int,
  `Item_name` varchar(255),
  `Rarity` varchar(255),
  `Cost` int,
  PRIMARY KEY (`Item_ID`)
);

CREATE TABLE `DAMAGE` (
  `PLayer_id` int,
  `Player_Dungeon_name` varchar(255),
  `Boss` varchar(255),
  `Boss_Dungeon_name` varchar(255),
  `Item_id` int,
  PRIMARY KEY (`PLayer_id`, `Boss`, `Player_Dungeon_name`, `Boss_Dungeon_name`, `Item_id`)
);

ALTER TABLE `Player` ADD FOREIGN KEY (`server_ip`) REFERENCES `SERVER` (`IP`) ON DELETE CASCADE ;

ALTER TABLE `Player` ADD FOREIGN KEY (`Class_name`) REFERENCES `Class` (`Class_name`);

ALTER TABLE `Player_Achievements` ADD FOREIGN KEY (`player_id`) REFERENCES `Player` (`player_id`) ON DELETE CASCADE;

ALTER TABLE `TRADE` ADD FOREIGN KEY (`seller_id`) REFERENCES `Player` (`player_id`) ON DELETE CASCADE;

ALTER TABLE `TRADE` ADD FOREIGN KEY (`buyer_id`) REFERENCES `Player` (`player_id`) ON DELETE CASCADE;

ALTER TABLE `BUY` ADD FOREIGN KEY (`Player_id`) REFERENCES `Player` (`player_id`) ON DELETE CASCADE;

ALTER TABLE `BUY` ADD FOREIGN KEY (`Item_id`) REFERENCES `Item` (`Item_ID`) ON DELETE CASCADE;

ALTER TABLE `Class_Weapons` ADD FOREIGN KEY (`Class_name`) REFERENCES `Class` (`Class_name`);

ALTER TABLE `Boss` ADD FOREIGN KEY (`Dungeon_name`) REFERENCES `Dungeon` (`Name`);

ALTER TABLE `NPC` ADD FOREIGN KEY (`NPC_name`) REFERENCES `NPC_Gender` (`NPC_name`);

ALTER TABLE `NPC` ADD FOREIGN KEY (`Location_id`) REFERENCES `Location` (`Location_id`)  ON DELETE CASCADE;

ALTER TABLE `Dungeon_Mob` ADD FOREIGN KEY (`Dungeon_Name`) REFERENCES `Dungeon` (`Name`);

ALTER TABLE `DROPS` ADD FOREIGN KEY (`Item_id`) REFERENCES `Item` (`Item_ID`) ON DELETE CASCADE;

ALTER TABLE `OWNED_BY` ADD FOREIGN KEY (`Item_ID`) REFERENCES `Item` (`Item_ID`) ON DELETE CASCADE;

ALTER TABLE `OWNED_BY` ADD FOREIGN KEY (`Player_id`) REFERENCES `Player` (`player_id`) ON DELETE CASCADE;

ALTER TABLE `DAMAGE` ADD FOREIGN KEY (`PLayer_id`) REFERENCES `Player` (`player_id`) ON DELETE CASCADE;

ALTER TABLE `DAMAGE` ADD FOREIGN KEY (`Player_Dungeon_name`) REFERENCES `Dungeon` (`Name`);

ALTER TABLE `DAMAGE` ADD FOREIGN KEY (`Item_id`) REFERENCES `Item` (`Item_ID`) ON DELETE CASCADE;

ALTER TABLE `Boss_Attacks` ADD FOREIGN KEY (`Dungeon_name`, `Boss`) REFERENCES `Boss` (`Dungeon_name`, `Name`) ON DELETE CASCADE;

ALTER TABLE `BUY` ADD FOREIGN KEY (`NPC_name`, `Location_id`) REFERENCES `NPC` (`NPC_name`, `Location_id`)  ON DELETE CASCADE;

ALTER TABLE `DAMAGE` ADD FOREIGN KEY (`Boss_Dungeon_name`, `Boss`) REFERENCES `Boss` (`Dungeon_name`, `Name`) ON DELETE CASCADE;


ALTER TABLE `DROPS` ADD FOREIGN KEY (`Dungeon_name`, `Boss_Name`) REFERENCES `Boss` (`Dungeon_name`, `Name`) ON DELETE CASCADE;

