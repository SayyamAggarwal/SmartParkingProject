CREATE DATABASE  IF NOT EXISTS `smart_parking` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `smart_parking`;
-- MySQL dump 10.13  Distrib 5.7.25, for Win32 (AMD64)
--
-- Host: localhost    Database: smart_parking
-- ------------------------------------------------------
-- Server version	5.7.25-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `issue_monthlypass`
--

DROP TABLE IF EXISTS `issue_monthlypass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `issue_monthlypass` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_number` varchar(45) NOT NULL,
  `vehicle_id` int(11) NOT NULL,
  `pass_id` int(11) NOT NULL,
  `issue_date` varchar(45) NOT NULL,
  `days` int(11) NOT NULL,
  `expiry_date` varchar(45) NOT NULL,
  `time` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vehicle_id_idx` (`vehicle_id`),
  KEY `bike_idx` (`pass_id`),
  CONSTRAINT `bike` FOREIGN KEY (`pass_id`) REFERENCES `monthly_pass` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cycle` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicle` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue_monthlypass`
--

LOCK TABLES `issue_monthlypass` WRITE;
/*!40000 ALTER TABLE `issue_monthlypass` DISABLE KEYS */;
/*!40000 ALTER TABLE `issue_monthlypass` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-18 16:15:31
