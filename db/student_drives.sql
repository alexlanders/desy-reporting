-- phpMyAdmin SQL Dump
-- version 4.6.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 22, 2016 at 11:46 PM
-- Server version: 10.1.13-MariaDB-cll-lve
-- PHP Version: 5.6.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `drivsdqw_desy01`
--

-- --------------------------------------------------------

--
-- Table structure for table `student_drives`
--

CREATE TABLE `student_drives` (
  `student_drive_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `instructor_id` int(11) DEFAULT NULL,
  `drive_date` date DEFAULT NULL,
  `has_corrective_lenses` tinyint(1) DEFAULT NULL,
  `has_permit` tinyint(1) DEFAULT NULL,
  `parent_signature` tinyint(1) DEFAULT NULL,
  `parent_signature_date` date DEFAULT NULL,
  `parent_signature_id` int(11) DEFAULT NULL,
  `student_drive_comments` text COLLATE utf8_unicode_ci,
  `drive_template_id` int(11) NOT NULL,
  `total_score` int(10) UNSIGNED DEFAULT NULL,
  `parent_practice_hours` float DEFAULT NULL,
  `parent_behaviors_practiced` text COLLATE utf8_unicode_ci,
  `student_drive_hours_driven` float DEFAULT NULL,
  `student_drive_hours_observed` float DEFAULT NULL,
  `student_drive_status` tinytext COLLATE utf8_unicode_ci,
  `last_updated` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `student_drives`
--

INSERT INTO `student_drives` (`student_drive_id`, `course_id`, `student_id`, `instructor_id`, `drive_date`, `has_corrective_lenses`, `has_permit`, `parent_signature`, `parent_signature_date`, `parent_signature_id`, `student_drive_comments`, `drive_template_id`, `total_score`, `parent_practice_hours`, `parent_behaviors_practiced`, `student_drive_hours_driven`, `student_drive_hours_observed`, `student_drive_status`, `last_updated`) VALUES
(1498, 1, 1, 2, '2016-02-09', 0, 1, 1, '2016-02-22', NULL, 'Test.', 1, NULL, 1, 'Turns, scanning intersections, parking', 1, 1.5, 'edited', '2016-04-06 19:17:41'),
(1499, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, NULL, 0.75, NULL, 'created', NULL),
(1500, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1501, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 4, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1502, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1503, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1504, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 7, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1505, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 8, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1511, 2, 9, 2, '2016-02-26', 0, 1, NULL, NULL, NULL, '', 9, NULL, NULL, NULL, 1, 0, 'submitted', '2016-02-26 19:04:40'),
(1512, 2, 9, 2, '2016-03-30', 0, 1, NULL, NULL, NULL, 'Another test.', 10, NULL, NULL, NULL, 1, 1, 'submitted', '2016-03-30 23:23:20'),
(1513, 2, 9, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 11, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1514, 2, 9, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 12, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1515, 2, 9, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 13, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1524, 1, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, 0.75, NULL, 'created', NULL),
(1525, 1, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1526, 1, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1527, 1, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 4, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1528, 1, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1529, 1, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1530, 1, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 7, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1531, 1, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 8, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1532, 2, 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 9, NULL, NULL, NULL, 1, NULL, 'created', NULL),
(1533, 2, 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 10, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1534, 2, 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 11, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1535, 2, 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 12, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1536, 2, 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 13, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1537, 1, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, 0.75, NULL, 'created', NULL),
(1538, 1, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL, NULL, NULL, 0.75, NULL, 'created', NULL),
(1539, 1, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1540, 1, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 4, NULL, NULL, NULL, 0.75, NULL, 'created', NULL),
(1541, 1, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1542, 1, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1543, 1, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 7, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1544, 1, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 8, NULL, NULL, NULL, 0.75, NULL, NULL, NULL),
(1600, 3, 7, 2, '2016-04-14', 1, 1, 1, '2016-05-05', NULL, 'This is a test. And another entry.And another on 4/20.', 14, NULL, NULL, NULL, 1, 1.5, 'edited', '2016-05-19 22:19:05'),
(1601, 3, 7, 2, '2016-04-18', 1, 1, 1, '2016-05-05', NULL, 'This is another test. And another on 4/18.', 15, NULL, NULL, NULL, 1, 1, 'edited', '2016-04-18 21:19:29'),
(1602, 3, 7, 2, '2016-04-19', 1, 1, NULL, NULL, NULL, 'Testing the new drive template.', 16, NULL, NULL, NULL, 1, 1, 'submitted', '2016-04-19 18:00:45'),
(1603, 3, 7, 2, '2016-04-19', 1, 1, NULL, NULL, NULL, 'Testing 123, testing 123.', 17, NULL, NULL, NULL, 1, 1.5, 'submitted', '2016-04-19 18:55:01'),
(1604, 3, 7, 2, '2016-04-18', 1, 1, NULL, NULL, NULL, 'Testing once again.', 18, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-19 19:09:50'),
(1605, 3, 18, 2, '2016-04-16', NULL, 1, NULL, NULL, NULL, 'Well done; curb parallel parking, backing straight, turns, acceleration,. Work on: LSMILE, legal stops (front limit), beginning turns.', 14, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-16 23:00:13'),
(1606, 3, 18, 2, '2016-04-23', NULL, 1, NULL, NULL, NULL, 'Practice: MSMOG, scanning intersections, turnabouts.', 15, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-23 23:06:06'),
(1607, 3, 18, 2, '2016-04-30', NULL, 1, NULL, NULL, NULL, 'Noce driving in traffic! Work on: rear zone checks, LP onturns, scanning intersections, rear-in perpendicular parking.', 16, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-30 23:13:23'),
(1608, 3, 18, 2, '2016-05-14', NULL, 1, NULL, NULL, NULL, 'Good: timing lights, scanning intersections. Work on: lane position on lane changes, rear-in perpendicular parking.', 17, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-14 23:07:31'),
(1609, 3, 18, 2, '2016-05-21', NULL, 1, NULL, NULL, NULL, 'Excellent freeway driving. Work on: refining skills.', 18, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-21 23:06:15'),
(1610, 3, 14, 2, '2016-04-15', NULL, 1, 1, '2016-06-11', 13, 'Done well: turning is very smooth, acceleration good. Work on: LSMILE, legal stops. Tes.', 14, NULL, NULL, NULL, 1, 1, 'edited', '2016-07-19 21:34:12'),
(1611, 3, 14, 2, '2016-04-22', NULL, 1, 1, '2016-06-11', 13, 'Practice: LSMILE, turnabouts, scanning intersections.', 15, NULL, NULL, NULL, 1, 1, 'submitted', '2016-04-23 01:04:13'),
(1612, 3, 14, 2, '2016-04-29', NULL, 1, NULL, NULL, NULL, 'Good: braking, accelerating, communication, speed control. Practice: scanning intersections, rear zone checks, MSMOG.', 16, NULL, NULL, NULL, 1, 1, 'submitted', '2016-04-30 01:03:05'),
(1613, 3, 14, 2, '2016-05-13', NULL, 1, NULL, NULL, NULL, 'Good: timing lights,  scanning intersections. Work on: over the shoulder on lateral moves (MSMOG), rear zone checks, rear-in perpendicular parking.', 17, NULL, NULL, NULL, 1, 1, 'submitted', '2016-05-14 01:12:25'),
(1614, 3, 14, 2, '2016-05-27', NULL, 1, NULL, NULL, NULL, 'Nice  freeway driving! Work on: rear-in perpendicular parking, rear zone checks, scanning intersections.', 18, NULL, NULL, NULL, 1, 1, 'submitted', '2016-05-28 01:08:57'),
(1615, 3, 16, 2, '2016-04-16', NULL, 1, NULL, NULL, NULL, 'Doing well: acceleration, braking, signals. Work on: LSMILE, push-pull steering, reference points.', 14, NULL, NULL, NULL, 1, 2, 'edited', '2016-04-16 23:06:23'),
(1616, 3, 16, 2, '2016-04-23', NULL, 1, NULL, NULL, NULL, 'Work on: right ', 15, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-23 23:08:05'),
(1617, 3, 16, 2, '2016-04-30', NULL, 1, NULL, NULL, NULL, 'Handling traffic very well. Work on: scanning intersections, rear zone checks, rear-in perpendicular parking.', 16, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-30 23:11:11'),
(1618, 3, 16, 2, '2016-05-14', NULL, 1, NULL, NULL, NULL, 'Good: timing lights, scanning intersections, lane changes. Work on: blind spot checks, rear-in perpendicular parking, rear zone checks.', 17, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-14 23:03:37'),
(1619, 3, 16, 2, '2016-05-21', NULL, 1, NULL, NULL, NULL, 'Very nice freeway driving. Work on: lane position on lane changes, blind spot checks, rear-in perpendicular parking.', 18, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-21 23:02:39'),
(1620, 3, 19, 2, '2016-07-16', NULL, 1, 1, '2016-07-16', 13, 'Doing well: accelerating, turns, smooth stops. Work on: LSMILE, reference points, legal stops.', 14, NULL, NULL, NULL, 1, 2, 'submitted', '2016-07-18 17:24:55'),
(1621, 3, 19, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 15, NULL, NULL, NULL, 1, NULL, 'created', NULL),
(1622, 3, 19, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 16, NULL, NULL, NULL, 1, NULL, 'created', NULL),
(1623, 3, 19, 2, '2016-05-15', NULL, 1, NULL, NULL, NULL, 'Good: timing lights, MSMOG, scanning intersections. Work on: rear-in perpendicular parking, lane position on lane changes, rear zone checks.', 17, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-15 17:02:11'),
(1624, 3, 19, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1625, 3, 21, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 14, NULL, NULL, NULL, NULL, NULL, 'created', NULL),
(1626, 3, 21, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 15, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1627, 3, 21, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 16, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1628, 3, 21, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 17, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1629, 3, 21, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1630, 3, 15, 2, '2016-04-15', NULL, 1, NULL, NULL, NULL, 'Good: hand position, acceleration, braking, signaling. Work on: LSMILE, turns, reference points.', 14, NULL, NULL, NULL, 1, 1, 'edited', '2016-04-16 01:08:14'),
(1631, 3, 15, 2, '2016-04-22', NULL, 1, NULL, NULL, NULL, 'Work on: signals, speed control, push-pull steering.', 15, NULL, NULL, NULL, 1, 1, 'submitted', '2016-04-23 01:06:44'),
(1632, 3, 15, 2, '2016-04-29', NULL, 1, NULL, NULL, NULL, 'Good: basic driving skills, following distance. Work on: charging lights, scanning intersections, rear zone checks, MSMOG.', 16, NULL, NULL, NULL, 1, 1, 'submitted', '2016-04-30 01:07:40'),
(1633, 3, 15, 2, '2016-05-13', NULL, 1, NULL, NULL, NULL, 'Good: timing lights, lane changes, MSMOG. Work on: rear zone checks, rear-in perpendicular parking, smooth acceleration if distracted.', 17, NULL, NULL, NULL, 1, 1, 'submitted', '2016-05-14 01:14:36'),
(1634, 3, 15, 2, '2016-05-27', NULL, 1, NULL, NULL, NULL, 'Kyle\'s in strong shape for the final drive. Work on: freeway driving, rear zone checks, rear-in perpendicular parking.', 18, NULL, NULL, NULL, 1, 1, 'submitted', '2016-05-28 01:10:36'),
(1635, 3, 17, 2, '2016-04-16', NULL, 1, NULL, NULL, NULL, 'Good: right side reference point, smooth acceleration ', 14, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-16 23:05:48'),
(1636, 3, 17, 2, '2016-04-23', NULL, 1, NULL, NULL, NULL, 'Work on: turnabouts, rear limit, LSMILE.', 15, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-23 23:09:42'),
(1637, 3, 17, 2, '2016-04-30', NULL, 1, NULL, NULL, NULL, 'Work on: lane position on right turns, speed control--too slow sometimes, rear zone checks.', 16, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-30 23:08:45'),
(1638, 3, 17, 2, '2016-05-14', NULL, 1, NULL, NULL, NULL, 'Did well: speed control, timing lights, turns. Work on: rear-in perpendicular parking, look first on lane changes, scanning intersections.', 17, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-14 23:05:50'),
(1639, 3, 17, 2, '2016-05-21', NULL, 1, NULL, NULL, NULL, 'Work on: smooth lane change turns, look before signal on lane changes, rear-in perpendicular parking.', 18, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-21 23:04:53'),
(1640, 3, 23, 2, '2016-04-17', NULL, 1, 1, '2016-06-12', 25, 'Strong: turning, accelerating, braking, lane position. Work on: LSMILE, reference points.', 14, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-17 22:28:12'),
(1641, 3, 23, 2, '2016-04-24', NULL, 1, NULL, NULL, NULL, 'Practice: parallel parking, left turns, scanning intersections.', 15, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-24 22:32:19'),
(1642, 3, 23, 2, '2016-05-01', NULL, 1, 1, '2016-06-19', 25, 'Welldone: timing lights, turning, following  gaps. Practice: lane position on right turns, speed control, scanning intersections, rear zone checks.', 16, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-01 22:40:03'),
(1643, 3, 23, 2, '2016-05-15', NULL, 1, NULL, NULL, NULL, 'Nicely done: scanning intersections, MSMOG, timing lights. Work on rear-in perpendicular parking, rear zone checks (including  blind spot checks).', 17, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-15 22:37:19'),
(1644, 3, 23, 2, '2016-05-22', NULL, 1, NULL, NULL, NULL, 'Good: freeway lane changes, following distance, enter/exit freeway. Work on: occasional velocitation, rear zone checks, rear-in perpendicular parking.', 18, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-22 22:34:57'),
(1645, 3, 22, 2, '2016-04-17', NULL, 1, 1, '2016-06-10', 25, 'Good: braking, acceleration, lane position. Work on: turning, LSMILE, reference points.', 14, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-17 22:31:26'),
(1646, 3, 22, 2, '2016-04-24', NULL, 1, 1, '2016-07-05', 25, 'Work on: speed control, wide turns, scanning intersections.', 15, NULL, NULL, NULL, 1, 2, 'edited', '2016-04-24 22:34:45'),
(1647, 3, 22, 2, '2016-05-01', NULL, 1, 1, '2016-06-10', 25, 'Good: timing lights, following distance, turns. Practice: scanning intersections, rear zone checks, MSMOG.', 16, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-01 22:37:15'),
(1648, 3, 22, 2, '2016-05-15', NULL, 1, 1, '2016-06-10', 25, 'Good: scanning intersections, lane changes, timing lights, speed control. Work on: rear-in perpendicular parking, rear zone checks.', 17, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-15 22:35:02'),
(1649, 3, 22, 2, '2016-05-22', NULL, 1, 1, '2016-07-19', 25, 'Nice freeway driving. Work on: occasional velocitation, rear zone checks, rear-in perpendicular parking.', 18, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-22 22:32:36'),
(1650, 3, 24, 2, '2016-04-17', NULL, 1, 1, '2016-06-13', 25, 'Did well: accelerating, braking, legal stops. Work on: push-pull steering, LSMILE, reference points, 8', 14, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-17 22:34:34'),
(1651, 3, 24, 2, '2016-04-24', NULL, 1, 1, '2016-06-13', 25, '', 15, NULL, NULL, NULL, 1, 2, 'submitted', '2016-04-24 22:35:46'),
(1652, 3, 24, 2, '2016-05-01', NULL, 1, NULL, NULL, NULL, 'Good: timing lights, lane position, MSMOG. Practice: rear zone checks, speed control, charging intersections  (minor issues).', 16, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-01 22:42:25'),
(1653, 3, 24, 2, '2016-05-15', NULL, 1, NULL, NULL, NULL, 'Doing well: speed control, timing lights, MSMOG, lane changes. Work on: scanning intersections, rear zone checks, rear-in perpendicular parking.', 17, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-15 22:39:09'),
(1654, 3, 24, 2, '2016-05-22', NULL, 1, NULL, NULL, NULL, 'Good: lane changes, following distance, enter/exit freeway. Work on: slight drifting on freeway, rear zone checks, rear-in perpendicular parking.', 18, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-22 22:30:42'),
(1655, 3, 1, 2, '2016-04-29', NULL, 1, NULL, NULL, NULL, 'This is a test of the cell service downtown.', 14, NULL, NULL, NULL, 1, 1, 'submitted', '2016-04-29 17:03:49'),
(1656, 3, 1, 2, '2016-05-03', NULL, 1, NULL, NULL, NULL, '', 15, NULL, NULL, NULL, 1, 0, 'edited', '2016-05-04 17:40:38'),
(1657, 3, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 16, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1658, 3, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 17, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1659, 3, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1660, 3, 20, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 14, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1661, 3, 20, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 15, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1662, 3, 20, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 16, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1663, 3, 20, 2, '2016-05-15', NULL, 1, NULL, NULL, NULL, 'Done well: timing lights, following distance, MSMOG, lane changes. Work on: scanning intersections, lane choice on left turns, lane position on right turns, rear zone checks.', 17, NULL, NULL, NULL, 1, 2, 'edited', '2016-05-15 19:11:24'),
(1664, 3, 20, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1670, 4, 4, 2, '2016-05-04', 1, 1, 1, '2016-05-25', 13, 'Test.', 14, NULL, NULL, NULL, 1, 1, 'edited', '2016-05-04 22:33:25'),
(1671, 4, 4, 2, '2016-05-04', 1, 1, 1, '2016-05-28', 13, 'Nice drive. Smart text is nice feature.', 15, NULL, NULL, NULL, 1, 1, 'edited', '2016-05-09 18:52:57'),
(1672, 4, 4, 2, '2016-05-16', 1, 1, 1, '2016-06-09', 13, 'Test.', 16, NULL, NULL, NULL, 1, 2, 'submitted', '2016-05-16 17:25:16'),
(1673, 4, 4, 2, '2016-05-27', 1, 1, NULL, NULL, NULL, 'This is a test of the new parent website. Another test of comments.', 17, NULL, NULL, NULL, 1, 1.5, 'edited', '2016-07-18 17:34:29'),
(1674, 4, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, NULL, NULL, 1, NULL, 'created', NULL),
(1675, 4, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 14, NULL, NULL, NULL, 1, NULL, 'created', NULL),
(1676, 4, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 15, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1677, 4, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 16, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1678, 4, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 17, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1679, 4, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1680, 4, 6, 2, '2016-05-09', 1, 1, NULL, NULL, NULL, 'Things to work on here.', 14, NULL, NULL, NULL, 1, 1.5, 'submitted', '2016-05-10 16:22:51'),
(1681, 4, 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 15, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1682, 4, 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 16, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1683, 4, 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 17, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1684, 4, 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1685, 4, 9, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 14, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1686, 4, 9, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 15, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1687, 4, 9, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 16, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1688, 4, 9, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 17, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1689, 4, 9, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1690, 4, 7, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 14, NULL, NULL, NULL, 1, NULL, 'created', NULL),
(1691, 4, 7, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 15, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1692, 4, 7, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 16, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1693, 4, 7, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 17, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1694, 4, 7, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1695, 4, 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 14, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1696, 4, 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 15, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1697, 4, 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 16, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1698, 4, 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 17, NULL, NULL, NULL, 1, NULL, NULL, NULL),
(1699, 4, 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, NULL, NULL, 1, NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student_drives`
--
ALTER TABLE `student_drives`
  ADD PRIMARY KEY (`student_drive_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student_drives`
--
ALTER TABLE `student_drives`
  MODIFY `student_drive_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1700;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
