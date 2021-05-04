-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 04, 2021 at 09:52 PM
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
  `VaccineBrand` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`AppointmentID`, `UserID`, `Campus`, `AppointmentDate`, `AppointmentTime`, `VaccineBrand`) VALUES
(1039, 1001, 'Kent', '2021-05-07', '08:00:00', 'Pfizer'),
(1040, 1001, 'Kent', '2021-05-28', '08:00:00', 'Pfizer');

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
  `NumberOrder` int(11) NOT NULL,
  `deliveryDate` date DEFAULT NULL,
  `OrderPlaced` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `campus`
--

INSERT INTO `campus` (`CampusName`, `isRegional`, `VaccinesOnHand`, `VaccinesGiven`, `Revenue`, `VaccineBrand`, `NumberOrder`, `deliveryDate`, `OrderPlaced`) VALUES
('East Liverpool', 1, 50, 0, 0, 'Moderna', 0, NULL, 0),
('Geauga', 1, 50, 0, 0, 'Johnson&Johnson', 0, NULL, 0),
('Kent', 0, 148, 1, 120, 'Pfizer', 88, '2021-05-09', 1),
('Salem', 1, 50, 0, 0, 'Pfizer', 0, NULL, 0),
('Stark', 1, 50, 0, 0, 'Johnson&Johnson', 0, NULL, 0),
('Trumbull', 1, 50, 0, 0, 'Moderna', 0, NULL, 0),
('Tuscarawas', 1, 50, 0, 0, 'Pfizer', 0, NULL, 0);

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
('example3@kent.edu', 'Password', 1003, 0),
('rsilvey2@kent.edu', 'Password', 1004, 0),
('csmit292@kent.edu', 'Password', 1005, 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `Name` varchar(256) NOT NULL,
  `Insurance` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `Name`, `Insurance`) VALUES
(1000, 'Kaleb Miller', 1),
(1001, 'John doe', 1);

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
  MODIFY `AppointmentID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1041;

--
-- AUTO_INCREMENT for table `logins`
--
ALTER TABLE `logins`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1006;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
