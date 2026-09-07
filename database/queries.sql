-- ============================================================
-- TENNIS SPORTSRADAR - SQL ANALYSIS
-- ============================================================


-- ============================================================
-- COMPETITION ANALYSIS (7 Queries)
-- ============================================================

-- Q1. Count competitions by category
SELECT
    cat.category_name,
    COUNT(comp.competition_id) AS total_competitions
FROM categories cat
LEFT JOIN competitions comp
    ON cat.category_id = comp.category_id
GROUP BY cat.category_id, cat.category_name
ORDER BY total_competitions DESC;


-- Q2. List competitions with their categories
SELECT
    comp.competition_id,
    comp.competition_name,
    cat.category_name
FROM competitions comp
LEFT JOIN categories cat
    ON comp.category_id = cat.category_id
ORDER BY comp.competition_name;


-- Q3. Count competitions by gender
SELECT
    gender,
    COUNT(*) AS total_competitions
FROM competitions
GROUP BY gender
ORDER BY total_competitions DESC;


-- Q4. Count competitions by competition type
SELECT
    type,
    COUNT(*) AS total_competitions
FROM competitions
GROUP BY type
ORDER BY total_competitions DESC;


-- Q5. Find competitions that have a parent competition
SELECT
    competition_id,
    competition_name,
    parent_id
FROM competitions
WHERE parent_id IS NOT NULL
ORDER BY competition_name;


-- Q6. Find competitions without a parent competition
SELECT
    competition_id,
    competition_name,
    type,
    gender
FROM competitions
WHERE parent_id IS NULL
ORDER BY competition_name;


-- Q7. Competition summary by category and gender
SELECT
    cat.category_name,
    comp.gender,
    COUNT(comp.competition_id) AS total_competitions
FROM competitions comp
LEFT JOIN categories cat
    ON comp.category_id = cat.category_id
GROUP BY cat.category_name, comp.gender
ORDER BY cat.category_name, total_competitions DESC;



-- ============================================================
-- VENUE & COMPLEX ANALYSIS (7 Queries)
-- ============================================================

-- Q8. Count venues by country
SELECT
    country_name,
    COUNT(venue_id) AS total_venues
FROM venues
WHERE country_name IS NOT NULL
GROUP BY country_name
ORDER BY total_venues DESC;


-- Q9. List all complexes with their venues
SELECT
    c.complex_id,
    c.complex_name,
    v.venue_id,
    v.venue_name,
    v.city_name,
    v.country_name,
    v.timezone
FROM complexes c
JOIN venues v
    ON c.complex_id = v.complex_id
ORDER BY c.complex_name, v.venue_name;


-- Q10. Count venues in each complex
SELECT
    c.complex_name,
    COUNT(v.venue_id) AS total_venues
FROM complexes c
LEFT JOIN venues v
    ON c.complex_id = v.complex_id
GROUP BY c.complex_id, c.complex_name
ORDER BY total_venues DESC;


-- Q11. Find complexes with more than one venue
SELECT
    c.complex_name,
    COUNT(v.venue_id) AS total_venues
FROM complexes c
JOIN venues v
    ON c.complex_id = v.complex_id
GROUP BY c.complex_id, c.complex_name
HAVING COUNT(v.venue_id) > 1
ORDER BY total_venues DESC;


-- Q12. List venues by city
SELECT
    city_name,
    COUNT(venue_id) AS total_venues
FROM venues
WHERE city_name IS NOT NULL
GROUP BY city_name
ORDER BY total_venues DESC, city_name;


-- Q13. List venues by country and city
SELECT
    country_name,
    city_name,
    COUNT(venue_id) AS total_venues
FROM venues
GROUP BY country_name, city_name
ORDER BY country_name, city_name;


-- Q14. Find venues with their complete location information
SELECT
    venue_name,
    city_name,
    country_name,
    country_code,
    timezone
FROM venues
ORDER BY country_name, city_name, venue_name;



-- ============================================================
-- COMPETITOR RANKING ANALYSIS (6 Queries)
-- ============================================================

-- Q15. Top 10 competitors by ranking
SELECT
    c.name AS player_name,
    c.country,
    c.country_code,
    r.rank,
    r.points,
    r.movement,
    r.competitions_played
FROM competitor_rankings r
JOIN competitors c
    ON r.competitor_id = c.competitor_id
ORDER BY r.rank ASC
LIMIT 10;


-- Q16. Top competitors by ranking points
SELECT
    c.name AS player_name,
    c.country,
    r.rank,
    r.points
FROM competitor_rankings r
JOIN competitors c
    ON r.competitor_id = c.competitor_id
ORDER BY r.points DESC
LIMIT 10;


-- Q17. Competitors with the biggest positive movement
SELECT
    c.name AS player_name,
    c.country,
    r.rank,
    r.movement,
    r.points
FROM competitor_rankings r
JOIN competitors c
    ON r.competitor_id = c.competitor_id
WHERE r.movement > 0
ORDER BY r.movement DESC;


-- Q18. Competitors with negative ranking movement
SELECT
    c.name AS player_name,
    c.country,
    r.rank,
    r.movement,
    r.points
FROM competitor_rankings r
JOIN competitors c
    ON r.competitor_id = c.competitor_id
WHERE r.movement < 0
ORDER BY r.movement ASC;


-- Q19. Average ranking points by country
SELECT
    c.country,
    COUNT(c.competitor_id) AS total_competitors,
    ROUND(AVG(r.points), 2) AS average_points
FROM competitors c
JOIN competitor_rankings r
    ON c.competitor_id = r.competitor_id
GROUP BY c.country
ORDER BY average_points DESC;


-- Q20. Competitors ranked with points and competitions played
SELECT
    c.name AS player_name,
    c.country,
    r.rank,
    r.points,
    r.competitions_played
FROM competitors c
JOIN competitor_rankings r
    ON c.competitor_id = r.competitor_id
ORDER BY r.rank ASC;