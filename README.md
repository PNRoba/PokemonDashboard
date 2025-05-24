# PokemonDashboard

## Task details:
### 1. Collect information about Pokemons:
   Chosen mode: Easy

### 2. Find the Pokemon which is the most effective companion through all generations (rank the pokemons from best to worst):
   Chosen mode: Hard

   Although I did not know anything about pokemon fighting prior to this project, I did my best to learn as I was completing the task. Do forgive me if my solution is not entirely accurate as most of the information I found was posted by and for people who have some prior knowledge of the battle mechanics.
   I do want to explain how i came to my solution.

   My solution was to calculate for each pokemon the sum of best damage dealt against each pokemon and then divide it by the total count of pokemon in the csv. That way each pokemon gets a sort of score based on the average damage it can deal when choosing the best attack in a fight against each pokemon.

   I tried being as close to the formula from the linked documentation as possible with the given data, which ended up resulting in:
   
   > (attack/defence) * multiplier

   The multiplier is calculated based on the attacker and defender types (based on the type multiplier table). For dual type pokemon the _best_multiplier_ function returns the attackers type and multiplier of the best case scenario. Later the chosen attackers type is used to determine if the attack is a <ins>physical</ins> or <ins>special</ins> and then choose to use the respective atrack and damage for the formula.

### 3. Create a dashboard according to your vision, adding the rank position, so the user could filter data and see which type of Pokemon is the most suited for him:
   Chosen mode: Normal

   The Pokemon Dashboard: https://lookerstudio.google.com/reporting/fb9bfef9-f403-4e18-8924-6a261ec37f92

   I decided to try out Google Looker Studio as I have not used it prior to this task. The generated csv file used in the report can be found in this repository under the name _output.csv_ as well as is shared as a google spreadsheet so it could be linked to the report: https://docs.google.com/spreadsheets/d/1w4B1GpEWUBBJza5ZAC7qnW0Fg21JlZedXRyUol0HRhM/edit?usp=sharing

   It has 2 sections - _Overall Pokemon Stats_ and I also felt like it could be beneficial to let the user select 2 pokemon to compare their stats in the section called _Compating Pokemon_. _Overall Pokemon Stats_ as a default shows pokemon serial number, name and damage score all ordered in descending order based on damage score, therefore showing the most effective pokemon against all other pokemons from the given csv. The section could also be used to filter the pokemon list to find pokemon of specific types or abilities, which, once found, can be compared in the pokemon comparing section.

   _Compating Pokemon_ contains a dropdown where you can select the name of the pokemon, which then will filter out all the pokemon with that name that was in the csv. In case there are more than one, there is another dropdown where you can select a specific serial number of the filtered pokemon, whic then will result in showing the stats of that specific pokemon. Stats like ATK, SP_ATK, DEF, SP_DEF, HP will be coloured in a tone from red (meaning the value is closer to 0) to green (meaning the value is closer to the max value in that field from the data in the given csv). That is to show visual comparison of the pokemon stats.

   
