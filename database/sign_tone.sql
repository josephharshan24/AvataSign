-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 18, 2025 at 11:34 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `sign_tone`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `ga_gesture`
--

CREATE TABLE `ga_gesture` (
  `id` int(11) NOT NULL,
  `gesture` varchar(50) NOT NULL,
  `fname` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ga_gesture`
--

INSERT INTO `ga_gesture` (`id`, `gesture`, `fname`) VALUES
(1, 'hi, welcome', 'f1.csv'),
(2, 'Very Super', 'f2.csv'),
(3, 'Peace', 'f3.csv'),
(4, 'How are you?', 'f4.csv'),
(5, 'call you', 'f5.csv'),
(6, 'stop', 'f6.csv');

-- --------------------------------------------------------

--
-- Table structure for table `sign_image`
--

CREATE TABLE `sign_image` (
  `id` int(11) NOT NULL,
  `message` varchar(200) NOT NULL,
  `image_file` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sign_image`
--

INSERT INTO `sign_image` (`id`, `message`, `image_file`) VALUES
(1, 'hi welcome', 'F1.gif'),
(2, 'Hello.', 'F2.gif'),
(3, 'Thank you so much', 'F3.gif');

-- --------------------------------------------------------

--
-- Table structure for table `sign_word`
--

CREATE TABLE `sign_word` (
  `id` int(11) NOT NULL,
  `sign` varchar(50) NOT NULL,
  `language` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sign_word`
--

