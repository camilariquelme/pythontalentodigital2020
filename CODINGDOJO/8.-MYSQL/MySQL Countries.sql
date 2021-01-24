use world;
 -- ¿Qué consulta harías para obtener todos los países que hablan esloveno? 
 -- Tu consulta debe devolver el nombre del país, el idioma y el porcentaje de idioma
 -- Tu consulta debe organizar el resultado por porcentaje de idioma en orden descendente. (1)

select * from languages where language like '%loven%';
select * from languages where language = 'slovene';

select * from countries
where id in (16,96,107,200)
;

select * from languages
inner join countries
on languages.country_id = countries.id
where language = 'Slovene'
;
select countries.name, languages.language, languages.percentage 
from languages
inner join countries
on languages.country_id = countries.id
where language = 'Slovene'
order by languages.percentage desc
;

-- ¿Qué consulta ejecutarías para mostrar el número total de ciudades para cada país? 
-- Su consulta debe devolver el nombre del país y el número total de ciudades.
-- Tu consulta debe organizar el resultado por el número de ciudades en orden descendente. (3)

select * from countries;

select count(cities.id) , countries.name from cities
inner join countries on cities.country_id = countries.id
group by countries.id
order by 1 desc;


--  ¿Qué consulta harías para obtener todas las ciudades de México con una población de más de 500,000?
-- Tu consulta debe organizar el resultado por población en orden descendente.

select cities.* from cities
inner join countries on cities.country_id = countries.id
where countries.id = 136 and cities.population > 500000
order by 5 desc
;

-- ¿Qué consulta ejecutarías para obtener todos los idiomas en cada país con un porcentaje superior al 89%? 
-- Tu consulta debe organizar el resultado por porcentaje en orden descendente. (1)

select countries.name, languages.language, languages.percentage 
from languages
inner join countries on languages.country_id = countries.id
where languages.percentage > 89
order by languages.percentage desc
;

-- ¿Qué consulta haría para obtener todos los países con un área de superficie inferior a 501 
-- y una población superior a 100,000? (2)

select countries.* from countries
where countries.surface_area < 501 and countries.population >100000
;

-- ¿Qué consulta harías para obtener países con solo Monarquía Constitucional con un 
-- capital superior a 200 y una esperanza de vida superior a 75 años? (1)

select countries.name, countries.government_form, countries.capital, countries.life_expectancy from countries
where countries.government_form = 'Constitutional Monarchy' and countries.capital > 200 and countries.life_expectancy > 75
;

-- ¿Qué consulta harías para obtener todas las ciudades de Argentina dentro del distrito de Buenos Aires 
-- y tener una población superior a 500,000? 
-- La consulta debe devolver el nombre del país, el nombre de la ciudad, el distrito y la población. (2)alter

select * from cities;

select countries.name, cities.name,cities.district,cities.population from cities
inner join countries on cities.country_id = countries.id
where countries.id = 9 and cities.population > 500000 and cities.district ='Buenos Aires'
;

-- ¿Qué consulta harías para resumir el número de países en cada región? 
-- La consulta debe mostrar el nombre de la región y el número de países. 
-- Además, la consulta debe organizar el resultado por el número de países en orden descendente. (2)

select count(cities.id), countries.region from cities
inner join countries on cities.country_id = countries.id
group by countries.id
order by 1 desc;