# File containing all of the sql queries that handle
# creation and deletion of tables

inserts = {"Economies": "INSERT INTO Economies VALUES(?" + 98 * ", ?" + ");",
           "Picks": "INSERT INTO Picks Values(?" + 16 * ", ?" + ");",
           "Players": "INSERT INTO Players Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",
           "Results": "INSERT INTO Results Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"}


creations = {
    "Economies": """CREATE TABLE Economies (
  date TEXT NOT NULL,
  match_id INTEGER,
  event_id INTEGER,
  team_1 TEXT NOT NULL,
  team_2 TEXT NOT NULL,
  best_of INTEGER,
  _map TEXT NOT NULL,
  t1_start TEXT NOT NULL,
  t2_start TEXT NOT NULL,
  round_1_t1 INTEGER,
  round_2_t1 INTEGER,
  round_3_t1 INTEGER,
  round_4_t1 INTEGER,
  round_5_t1 INTEGER,
  round_6_t1 INTEGER,
  round_7_t1 INTEGER,
  round_8_t1 INTEGER,
  round_9_t1 INTEGER,
  round_10_t1 INTEGER,
  round_11_t1 INTEGER,
  round_12_t1 INTEGER,
  round_13_t1 INTEGER,
  round_14_t1 INTEGER,
  round_15_t1 INTEGER,
  round_16_t1 INTEGER,
  round_17_t1 INTEGER,
  round_18_t1 INTEGER,
  round_19_t1 INTEGER,
  round_20_t1 INTEGER,
  round_21_t1 INTEGER,
  round_22_t1 INTEGER,
  round_23_t1 INTEGER,
  round_24_t1 INTEGER,
  round_25_t1 INTEGER,
  round_26_t1 INTEGER,
  round_27_t1 INTEGER,
  round_28_t1 INTEGER,
  round_29_t1 INTEGER,
  round_30_t INTEGER1,
  round_1_t2 INTEGER,
  round_2_t2 INTEGER,
  round_3_t2 INTEGER,
  round_4_t2 INTEGER,
  round_5_t2 INTEGER,
  round_6_t2 INTEGER,
  round_7_t2 INTEGER,
  round_8_t2 INTEGER,
  round_9_t2 INTEGER,
  round_10_t2 INTEGER,
  round_11_t2 INTEGER,
  round_12_t2 INTEGER,
  round_13_t2 INTEGER,
  round_14_t2 INTEGER,
  round_15_t2 INTEGER,
  round_16_t2 INTEGER,
  round_17_t2 INTEGER,
  round_18_t2 INTEGER,
  round_19_t2 INTEGER,
  round_20_t2 INTEGER,
  round_21_t2 INTEGER,
  round_22_t2 INTEGER,
  round_23_t2 INTEGER,
  round_24_t2 INTEGER,
  round_25_t2 INTEGER,
  round_26_t2 INTEGER,
  round_27_t2 INTEGER,
  round_28_t2 INTEGER,
  round_29_t2 INTEGER,
  round_30_t2 INTEGER,
  round_1_winner INTEGER,
  round_2_winner INTEGER,
  round_3_winner INTEGER,
  round_4_winner INTEGER,
  round_5_winner INTEGER,
  round_6_winner INTEGER,
  round_7_winner INTEGER,
  round_8_winner INTEGER,
  round_9_winner INTEGER,
  round_10_winner INTEGER,
  round_11_winner INTEGER,
  round_12_winner INTEGER,
  round_13_winner INTEGER,
  round_14_winner INTEGER,
  round_15_winner INTEGER,
  round_16_winner INTEGER,
  round_17_winner INTEGER,
  round_18_winner INTEGER,
  round_19_winner INTEGER,
  round_20_winner INTEGER,
  round_21_winner INTEGER,
  round_22_winner INTEGER,
  round_23_winner INTEGER,
  round_24_winner INTEGER,
  round_25_winner INTEGER,
  round_26_winner INTEGER,
  round_27_winner INTEGER,
  round_28_winner INTEGER,
  round_29_winner INTEGER,
  round_30_winner INTEGER,
  PRIMARY KEY(match_id, _map)
);""",

    "Picks": """CREATE TABLE Picks (
  date TEXT NOT NULL,
  team_1 TEXT NOT NULL,
  team_2 TEXT NOT NULL,
  inverted_teams INTEGER,
  match_id INTEGER,
  event_id INTEGER,
  best_of INTEGER,
  system INTEGER,
  t1_removed_1 TEXT NOT NULL,
  t1_removed_2 TEXT NOT NULL,
  t1_removed_3 TEXT NOT NULL,
  t2_removed_1 TEXT NOT NULL,
  t2_removed_2 TEXT NOT NULL,
  t2_removed_3 TEXT NOT NULL,
  t1_picked_1 TEXT NOT NULL,
  t2_picked_1 TEXT NOT NULL,
  left_over TEXT NOT NULL,
  PRIMARY KEY(match_id)
);""",
    "Players": """CREATE TABLE Players (
  date TEXT NOT NULL,
  player_name TEXT NOT NULL,
  team TEXT NOT NULL,
  opponent TEXT NOT NULL,
  country TEXT NOT NULL,
  player_id INTEGER,
  match_id INTEGER,
  event_id INTEGER,
  event_name TEXT NOT NULL,
  best_of INTEGER,
  map_1 TEXT NOT NULL,
  map_2 TEXT NOT NULL,
  map_3 TEXT NOT NULL,
  kills INTEGER,
  assists INTEGER,
  deaths INTEGER,
  hs INTEGER,
  flash_assists INTEGER,
  kast REAL,
  kddiff INTEGER,
  adr REAL,
  fkdiff INTEGER,
  rating REAL,
  m1_kills INTEGER,
  m1_assists INTEGER,
  m1_deaths INTEGER,
  m1_hs INTEGER,
  m1_flash_assists INTEGER,
  m1_kast REAL,
  m1_kddiff INTEGER,
  m1_adr REAL,
  m1_fkdiff INTEGER,
  m1_rating REAL,
  m2_kills INTEGER,
  m2_assists INTEGER,
  m2_deaths INTEGER,
  m2_hs INTEGER,
  m2_flash_assists INTEGER,
  m2_kast REAL,
  m2_kddiff INTEGER,
  m2_adr REAL,
  m2_fkdiff INTEGER,
  m2_rating REAL,
  m3_kills INTEGER,
  m3_assists INTEGER,
  m3_deaths INTEGER,
  m3_hs INTEGER,
  m3_flash_assists INTEGER,
  m3_kast REAL,
  m3_kddiff INTEGER,
  m3_adr REAL,
  m3_fkdiff INTEGER,
  m3_rating REAL,
  kills_ct INTEGER,
  deaths_ct INTEGER,
  kddiff_ct INTEGER,
  adr_ct REAL,
  kast_ct REAL,
  rating_ct REAL,
  kills_t INTEGER,
  deaths_t INTEGER,
  kddiff_t INTEGER,
  adr_t REAL,
  kast_t REAL,
  rating_t REAL,
  m1_kills_ct INTEGER,
  m1_deaths_ct INTEGER,
  m1_kddiff_ct INTEGER,
  m1_adr_ct REAL,
  m1_kast_ct REAL,
  m1_rating_ct REAL,
  m1_kills_t INTEGER,
  m1_deaths_t INTEGER,
  m1_kddiff_t INTEGER,
  m1_adr_t REAL,
  m1_kast_t REAL,
  m1_rating_t REAL,
  m2_kills_ct INTEGER,
  m2_deaths_ct INTEGER,
  m2_kddiff_ct INTEGER,
  m2_adr_ct REAL,
  m2_kast_ct REAL,
  m2_rating_ct REAL,
  m2_kills_t INTEGER,
  m2_deaths_t INTEGER,
  m2_kddiff_t INTEGER,
  m2_adr_t REAL,
  m2_kast_t REAL,
  m2_rating_t REAL,
  m3_kills_ct INTEGER,
  m3_deaths_ct INTEGER,
  m3_kddiff_ct INTEGER,
  m3_adr_ct REAL,
  m3_kast_ct REAL,
  m3_rating_ct REAL,
  m3_kills_t INTEGER,
  m3_deaths_t INTEGER,
  m3_kddiff_t INTEGER,
  m3_adr_t REAL,
  m3_kast_t REAL,
  m3_rating_t REAL,
  PRIMARY KEY(match_id, player_id)
);""",
    "Results": """CREATE TABLE Results (
  date TEXT NOT NULL,
  team_1 TEXT NOT NULL,
  team_2 TEXT NOT NULL,
  _map TEXT NOT NULL,
  result_1 INTEGER,
  result_2 INTEGER,
  map_winner INTEGER,
  starting_ct INTEGER,
  ct_1 INTEGER,
  t_2 INTEGER,
  t_1 INTEGER,
  ct_2 INTEGER,
  event_id INTEGER,
  match_id INTEGER,
  rank_1 INTEGER,
  rank_2 INTEGER,
  map_wins_1 INTEGER,
  map_wins_2 INTEGER,
  match_winner INTEGER,
  PRIMARY KEY(match_id, _map)
)"""
}

inDB = """SELECT name
       FROM sqlite_master 
       WHERE type='table' AND name=?;"""

drop_table = """DROP TABLE ?;"""
