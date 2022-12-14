# File containing all sql queries for data analysis

# Calculated over the entire database
# returns:
# total_better_rank_wins, total_games
sql_better_rank_wins = """
  SELECT
  (SELECT count(*)
  FROM Results
  WHERE (match_winner = 1 AND rank_1 < rank_2) OR (match_winner = 2 AND rank_1 > rank_2))
  as better_rank_wins, 
  (SELECT count(*)
  FROM Results)
  as total_games
"""

# inputs:
# max_rank, min_rank
# returns:
# total_better_rank_wins, total_games
sql_incremented_better_rank_wins = """
SELECT
(SELECT count(*)
FROM Results
WHERE ((match_winner = 1 AND rank_1 < rank_2) OR (match_winner = 2 AND rank_1 > rank_2)) AND :min_rank <= rank_1 AND rank_1 <= :max_rank AND :min_rank <= rank_2 AND rank_2 <= :max_rank)
as better_rank_wins, 
(SELECT count(*)
FROM Results
where :min_rank <= rank_1 AND rank_1 <= :max_rank AND :min_rank <= rank_2 AND rank_2 <= :max_rank)
as total_games"""

# inputs:
# :rank
# returns
# wins, losses
sql_single_rank_wins_and_losses = """
SELECT 
(SELECT count(*)
FROM Results
WHERE (match_winner = 1 AND rank_1 = :rank) OR (match_winner = 2 AND rank_2 = :rank))
as wins_count,
(SELECT count(*)
FROM Results
WHERE (match_winner = 2 AND rank_1 = :rank) OR (match_winner = 1 AND rank_2 = :rank))
as loss_count"""

# returns
# max_rank
sql_max_rank = """
SELECT MAX(
(SELECT MAX(rank_1) as rank
FROM Results
	UNION
SELECT MAX(rank_2) as rank
FROM Results))
as max_rank"""
