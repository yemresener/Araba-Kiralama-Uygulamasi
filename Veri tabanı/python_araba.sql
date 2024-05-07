-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 07 May 2024, 21:05:54
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `python_araba`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `admins`
--

CREATE TABLE `admins` (
  `id` int(11) NOT NULL,
  `ad` varchar(30) NOT NULL,
  `sifre` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `admins`
--

INSERT INTO `admins` (`id`, `ad`, `sifre`) VALUES
(1, 'emre', '12345'),
(2, 'Cardinal', 'Tom B. Erichsen'),
(8, 'dsfsd', 'fddfgdf'),
(9, 'emer', '123');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `arabalar`
--

CREATE TABLE `arabalar` (
  `ARAC_ID` int(11) NOT NULL,
  `MARKA` varchar(50) NOT NULL,
  `MODEL` varchar(50) NOT NULL,
  `VITES` varchar(50) NOT NULL,
  `KIRA_DURUMU` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `arabalar`
--

INSERT INTO `arabalar` (`ARAC_ID`, `MARKA`, `MODEL`, `VITES`, `KIRA_DURUMU`) VALUES
(1, 'BMW', 'A3', 'Otamatik', 'Müsait');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `arabalar_tablosu`
--

CREATE TABLE `arabalar_tablosu` (
  `Arac_id` int(11) NOT NULL,
  `marka` text NOT NULL,
  `km` text NOT NULL,
  `vites` text NOT NULL,
  `saatlik` text NOT NULL,
  `gunluk` text NOT NULL,
  `kira` text NOT NULL,
  `kiralayan_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `arabalar_tablosu`
--

INSERT INTO `arabalar_tablosu` (`Arac_id`, `marka`, `km`, `vites`, `saatlik`, `gunluk`, `kira`, `kiralayan_id`) VALUES
(16, '12231213213', 'qwewqe', 'ads', '200', '550', 'Kiralı', 14),
(35, 'BMW', '12000', 'MANUEL', '120', '500', 'Kiralı', 20),
(36, 'BMW', '12000', 'oto', '120', '500', 'Kiralı', 19),
(37, 'BMW', '12000', 'MANUEL', '1', '500', 'Kiralı', 1),
(38, '12231213213', 'qwewqe', 'ads', '50', '500', 'Kiralı', 21),
(39, '12312', 'qwewqe', 'ads', '100', '200', 'Müsait', 0),
(42, 'Müsait4', 'Müsait', 'Müsait', '20', '20', 'Kiralı', 1),
(45, 'qweqweqw', 'eqweqweqw', 'eqweqwe', '20', '20', 'Kiralı', 1),
(46, 'Müsait2', 'Müsait', 'Müsait', '20', '20', 'Müsait', 0),
(50, 'yunus', 'yunus', 'yunus', 'yunus', 'yunus', 'yunus', 11),
(51, 'Nutri-B', 'Vitamin', 'Şurup', 'Tok karına Günde 1 kere', '12.11.2028', '12', 0);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `customers`
--

CREATE TABLE `customers` (
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kullanicilar`
--

CREATE TABLE `kullanicilar` (
  `id` int(11) NOT NULL,
  `ad` text NOT NULL,
  `sifre` text NOT NULL,
  `telno` text NOT NULL,
  `bakiye` int(40) NOT NULL DEFAULT 500
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `kullanicilar`
--

INSERT INTO `kullanicilar` (`id`, `ad`, `sifre`, `telno`, `bakiye`) VALUES
(1, 'emre', '1', '1', 121),
(2, 'emres', '1', '1', -1740),
(10, 'asd', 'a', 'dsa', 20),
(11, 'asdf', 'asd', 'asd', 500),
(12, '', 'faasf', 'dsa', 500),
(13, '        ', 'hdg', 'gfd', 500),
(14, '1', '1', '1', 180),
(15, ' 1', '1', ' 1', 500),
(16, 'yunus', '12', 'emre', 500),
(17, 'qweqw', 'qweqwweq', 'eqweqwe', 500),
(18, 'yunusdot', 'yunus', 'dot', 500),
(19, 'ahmet', '123', '20200', 140),
(20, 'ahmet1', '12', '2020202', 94),
(21, 'yunus1', 'emre', '12312', 300);

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `arabalar`
--
ALTER TABLE `arabalar`
  ADD PRIMARY KEY (`ARAC_ID`);

--
-- Tablo için indeksler `arabalar_tablosu`
--
ALTER TABLE `arabalar_tablosu`
  ADD PRIMARY KEY (`Arac_id`);

--
-- Tablo için indeksler `kullanicilar`
--
ALTER TABLE `kullanicilar`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `admins`
--
ALTER TABLE `admins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Tablo için AUTO_INCREMENT değeri `arabalar`
--
ALTER TABLE `arabalar`
  MODIFY `ARAC_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Tablo için AUTO_INCREMENT değeri `arabalar_tablosu`
--
ALTER TABLE `arabalar_tablosu`
  MODIFY `Arac_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- Tablo için AUTO_INCREMENT değeri `kullanicilar`
--
ALTER TABLE `kullanicilar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
