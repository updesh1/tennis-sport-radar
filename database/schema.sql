CREATE TABLE IF NOT EXISTS categories (
    category_id VARCHAR(50) PRIMARY KEY,
    category_name VARCHAR(150) NOT NULL
);

CREATE TABLE IF NOT EXISTS competitions (
    competition_id VARCHAR(50) PRIMARY KEY,
    competition_name VARCHAR(200) NOT NULL,
    parent_id VARCHAR(50),
    type VARCHAR(50),
    gender VARCHAR(20),
    category_id VARCHAR(50),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE IF NOT EXISTS complexes (
    complex_id VARCHAR(50) PRIMARY KEY,
    complex_name VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS venues (
    venue_id VARCHAR(50) PRIMARY KEY,
    venue_name VARCHAR(200) NOT NULL,
    city_name VARCHAR(100),
    country_name VARCHAR(100),
    country_code VARCHAR(10),
    timezone VARCHAR(50),
    complex_id VARCHAR(50),
    FOREIGN KEY (complex_id) REFERENCES complexes(complex_id)
);

CREATE TABLE IF NOT EXISTS competitors (
    competitor_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    country VARCHAR(100),
    country_code VARCHAR(10),
    abbreviation VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS competitor_rankings (
    rank_id SERIAL PRIMARY KEY,
    rank INT,
    movement INT,
    points INT,
    competitions_played INT,
    competitor_id VARCHAR(50),
    FOREIGN KEY (competitor_id) REFERENCES competitors(competitor_id)
);