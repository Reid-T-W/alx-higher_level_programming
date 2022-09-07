-- Lists all cities contained in a database
SELECT id, name, states_id
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id
