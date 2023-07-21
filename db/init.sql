CREATE DATABASE IF NOT EXISTS `shorten_url`;
USE `shorten_url`;

DROP TABLE IF EXISTS `url_list`;
CREATE TABLE `url_list` (
  `id` int NOT NULL AUTO_INCREMENT,
  `url` varchar(256) NOT NULL,
  `url_short` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;