SELECT 
    c.name AS player_name,
    c.country,
    c.country_code,
    r.rank,
    r.points,
    r.movement,
    r.competitions_played
FROM competitor_rankings r
JOIN competitors c ON r.competitor_id = c.competitor_id
ORDER BY r.rank ASC
LIMIT 10;

SELECT 
    cat.category_name,
    COUNT(comp.competition_id) AS total_competitions
FROM categories cat
LEFT JOIN competitions comp ON cat.category_id = comp.category_id
GROUP BY cat.category_id, cat.category_name
ORDER BY total_competitions DESC;

SELECT 
    country_name,
    COUNT(venue_id) AS total_venues
FROM venues
WHERE country_name IS NOT NULL
GROUP BY country_name
ORDER BY total_venues DESC;

SELECT 
    c.complex_name,
    v.venue_name,
    v.city_name,
    v.country_name,
    v.timezone
FROM complexes c
JOIN venues v ON c.complex_id = v.complex_id
ORDER BY c.complex_name, v.venue_name;

SELECT 
    c.name AS player_name,
    c.country,
    r.rank,
    r.movement,
    r.points
FROM competitor_rankings r
JOIN competitors c ON r.competitor_id = c.competitor_id
ORDER BY r.movement DESC
LIMIT 10;