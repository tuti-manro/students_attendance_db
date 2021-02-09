-- MariaDB dump 10.17  Distrib 10.5.4-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: attendance_system
-- ------------------------------------------------------
-- Server version	10.5.4-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `examn_groups`
--

DROP TABLE IF EXISTS `examn_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `examn_groups` (
  `id_event` int(10) DEFAULT NULL,
  `id_group` varchar(5) DEFAULT NULL,
  `subject` varchar(100) DEFAULT NULL,
  KEY `fk_group_id_subject` (`id_group`,`subject`),
  KEY `fk_id_event_exm` (`id_event`),
  CONSTRAINT `fk_group_id_subject` FOREIGN KEY (`id_group`, `subject`) REFERENCES `subjects` (`id_group`, `subject`),
  CONSTRAINT `fk_id_event_exm` FOREIGN KEY (`id_event`) REFERENCES `record_dates` (`id_event`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examn_groups`
--

LOCK TABLES `examn_groups` WRITE;
/*!40000 ALTER TABLE `examn_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `examn_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `record_dates`
--

DROP TABLE IF EXISTS `record_dates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `record_dates` (
  `id_event` int(10) NOT NULL AUTO_INCREMENT,
  `description` varchar(50) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `date_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id_event`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `record_dates`
--

LOCK TABLES `record_dates` WRITE;
/*!40000 ALTER TABLE `record_dates` DISABLE KEYS */;
/*!40000 ALTER TABLE `record_dates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration`
--

DROP TABLE IF EXISTS `registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registration` (
  `id_group` varchar(5) NOT NULL,
  `student_id` int(5) NOT NULL,
  `subject` varchar(100) NOT NULL,
  PRIMARY KEY (`id_group`,`student_id`,`subject`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration`
--

LOCK TABLES `registration` WRITE;
/*!40000 ALTER TABLE `registration` DISABLE KEYS */;
/*!40000 ALTER TABLE `registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sk_key`
--

DROP TABLE IF EXISTS `sk_key`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sk_key` (
  `sk_key` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sk_key`
--

LOCK TABLES `sk_key` WRITE;
/*!40000 ALTER TABLE `sk_key` DISABLE KEYS */;
INSERT INTO `sk_key` VALUES ('6CD995A71B07488F9A3442C2AB97C278');
/*!40000 ALTER TABLE `sk_key` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `student_id` int(5) NOT NULL,
  `student_name` varchar(50) DEFAULT NULL,
  `student_last_name` varchar(100) DEFAULT NULL,
  `nfc_uid` bigint(13) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students_attendance`
--

DROP TABLE IF EXISTS `students_attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students_attendance` (
  `id_event` int(10) NOT NULL,
  `student_id` int(5) NOT NULL,
  `student_name` varchar(50) DEFAULT NULL,
  `student_last_name` varchar(100) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id_event`,`student_id`),
  KEY `fk_student_id` (`student_id`),
  CONSTRAINT `fk_id_event` FOREIGN KEY (`id_event`) REFERENCES `record_dates` (`id_event`) ON DELETE CASCADE,
  CONSTRAINT `fk_student_id` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students_attendance`
--

LOCK TABLES `students_attendance` WRITE;
/*!40000 ALTER TABLE `students_attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `students_attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subjects`
--

DROP TABLE IF EXISTS `subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subjects` (
  `id_group` varchar(5) NOT NULL,
  `subject` varchar(100) NOT NULL,
  PRIMARY KEY (`id_group`,`subject`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subjects`
--

LOCK TABLES `subjects` WRITE;
/*!40000 ALTER TABLE `subjects` DISABLE KEYS */;
/*!40000 ALTER TABLE `subjects` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-09 13:43:20
