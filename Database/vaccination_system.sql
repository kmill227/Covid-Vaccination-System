-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 02, 2021 at 04:51 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vaccination_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `AppointmentID` int(11) NOT NULL,
  `UserID` int(11) NOT NULL,
  `Campus` varchar(15) NOT NULL,
  `AppointmentDate` date NOT NULL,
  `AppointmentTime` time NOT NULL,
  `VaccineBrand` varchar(45) NOT NULL,
  `Complete` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`AppointmentID`, `UserID`, `Campus`, `AppointmentDate`, `AppointmentTime`, `VaccineBrand`, `Complete`) VALUES
(1000, 1000, 'Stark', '2021-05-03', '09:51:00', 'Johnson&Johnson', 0);

-- --------------------------------------------------------

--
-- Table structure for table `campus`
--

CREATE TABLE `campus` (
  `CampusName` varchar(15) NOT NULL,
  `isRegional` tinyint(1) NOT NULL,
  `VaccinesOnHand` int(4) NOT NULL,
  `VaccinesGiven` int(5) NOT NULL,
  `Revenue` int(8) NOT NULL,
  `VaccineBrand` varchar(45) NOT NULL,
  `deliveryDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `campus`
--

INSERT INTO `campus` (`CampusName`, `isRegional`, `VaccinesOnHand`, `VaccinesGiven`, `Revenue`, `VaccineBrand`, `deliveryDate`) VALUES
('East Liverpool', 1, 50, 0, 0, 'Moderna', NULL),
('Geauga', 1, 50, 0, 0, 'Johnson&Johnson', NULL),
('Kent', 0, 150, 0, 0, 'Pfizer', NULL),
('Salem', 1, 50, 0, 0, 'Pfizer', NULL),
('Stark', 1, 50, 0, 0, 'Johnson&Johnson', NULL),
('Trumbull', 1, 50, 0, 0, 'Moderna', NULL),
('Tuscarawas', 1, 50, 0, 0, 'Pfizer', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `logins`
--

CREATE TABLE `logins` (
  `Email` varchar(256) NOT NULL,
  `Password` varchar(16) NOT NULL,
  `ID` int(11) NOT NULL,
  `IsAdmin` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `logins`
--

INSERT INTO `logins` (`Email`, `Password`, `ID`, `IsAdmin`) VALUES
('kmill227@kent.edu', 'Password', 1000, 0),
('examplemail@kent.edu', 'Password', 1001, 0),
('example2@kent.edu', 'Password', 1002, 0),
('example3@kent.edu', 'Password', 1003, 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `Name` varchar(256) NOT NULL,
  `Vaccinations` int(1) NOT NULL,
  `Insurance` int(11) NOT NULL,
  `Brand` varchar(45) NOT NULL,
  `Completed` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `Name`, `Vaccinations`, `Insurance`, `Brand`, `Completed`) VALUES
(1000, 'Kaleb Miller', 0, 0, '', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`AppointmentID`);

--
-- Indexes for table `campus`
--
ALTER TABLE `campus`
  ADD PRIMARY KEY (`CampusName`);

--
-- Indexes for table `logins`
--
ALTER TABLE `logins`
  ADD PRIMARY KEY (`ID`) USING BTREE;

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `AppointmentID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1001;

--
-- AUTO_INCREMENT for table `logins`
--
ALTER TABLE `logins`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1004;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1001;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
