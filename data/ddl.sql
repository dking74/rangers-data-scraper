-- Table: public.Player

-- DROP TABLE IF EXISTS public."Player";

CREATE TABLE IF NOT EXISTS public."Player"
(
    player_id serial NOT NULL,
    first_name text COLLATE pg_catalog."default" NOT NULL,
    last_name text COLLATE pg_catalog."default" NOT NULL,
    logo text COLLATE pg_catalog."default",
    age integer NOT NULL,
    dob date NOT NULL,
    country character varying(2) COLLATE pg_catalog."default" DEFAULT 'US',
    "position" text COLLATE pg_catalog."default",
    bats character(1) COLLATE pg_catalog."default" DEFAULT 'R',
    throws character(1) COLLATE pg_catalog."default" DEFAULT 'R',
    height character varying(10) COLLATE pg_catalog."default",
    weight numeric(5,2),
    years integer,
    CONSTRAINT "Player_pkey" PRIMARY KEY (player_id),
    CONSTRAINT "First/Last/DOB" UNIQUE (first_name, last_name, dob),
    CONSTRAINT "Age >= 16 && Age < 60" CHECK (age >= 16 AND age < 60),
    CONSTRAINT "Years >= 1 && Years < 30" CHECK (years >= 1 AND years < 30),
    CONSTRAINT "Bats = 'R' || Bats = 'L' || Bats = 'S'" CHECK (bats = 'R'::bpchar OR bats = 'L'::bpchar OR bats = 'S'::bpchar),
    CONSTRAINT "Throws = 'R' || Throws = 'L'" CHECK (throws = 'R'::bpchar OR throws = 'L'::bpchar)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Player"
    OWNER to postgres;

CREATE INDEX IF NOT EXISTS idx_full_name_player ON public."Player" (first_name, last_name);


-- Table: public.Roster

-- DROP TABLE IF EXISTS public."Roster";

CREATE TABLE IF NOT EXISTS public."Roster"
(
    roster_id serial NOT NULL,
    year integer NOT NULL,
    player_id integer NOT NULL,
    CONSTRAINT "Roster_id_pk" PRIMARY KEY (roster_id),
    CONSTRAINT "Unique_year_player" UNIQUE (year, player_id),
    CONSTRAINT "Player_id_fk" FOREIGN KEY (player_id)
        REFERENCES public."Player" (player_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT "year >= 1900" CHECK (year >= 1900)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Roster"
    OWNER to postgres;


-- Table: public.PlayerBatYearResult

-- DROP TABLE IF EXISTS public."PlayerBatYearResult";

CREATE TABLE IF NOT EXISTS public."PlayerBatYearResult"
(
    player_bat_year_result_id bigserial NOT NULL,
    year integer NOT NULL,
    player_id integer NOT NULL,
    games integer DEFAULT 0,
    plate_appearances integer DEFAULT 0,
    at_bats integer DEFAULT 0,
    runs integer DEFAULT 0,
    hits integer DEFAULT 0,
    doubles integer DEFAULT 0,
    triples integer DEFAULT 0,
    home_runs integer DEFAULT 0,
    rbis integer DEFAULT 0,
    stolen_bases integer DEFAULT 0,
    caught_stealing integer DEFAULT 0,
    walks integer DEFAULT 0,
    strikeouts integer DEFAULT 0,
    batting_average numeric(3,3) DEFAULT 0,
    obp numeric(3,3) DEFAULT 0,
    slg numeric(3,3) DEFAULT 0,
    ops numeric(3,3) DEFAULT 0,
    ops_plus integer DEFAULT 0,
    total_bases integer DEFAULT 0,
    gdp integer DEFAULT 0,
    hbp integer DEFAULT 0,
    sacrifice_fly integer DEFAULT 0,
    ibb integer DEFAULT 0,
    CONSTRAINT "PlayerBatYearResult_pkey" PRIMARY KEY (player_bat_year_result_id),
    CONSTRAINT "Unique_year_player_player_bat_year_stats" UNIQUE (year, player_id),
    CONSTRAINT player_id FOREIGN KEY (player_id)
        REFERENCES public."Player" (player_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "at_bats >= 0" CHECK (at_bats >= 0),
    CONSTRAINT "batting_average >= 0" CHECK (batting_average >= 0::numeric),
    CONSTRAINT "caught_stealing >= 0" CHECK (caught_stealing >= 0),
    CONSTRAINT "doubles >= 0" CHECK (doubles >= 0),
    CONSTRAINT "games >= 0" CHECK (games >= 0),
    CONSTRAINT "gdp >= 0" CHECK (gdp >= 0),
    CONSTRAINT "hbp >= 0" CHECK (hbp >= 0),
    CONSTRAINT "hits >= 0" CHECK (hits >= 0),
    CONSTRAINT "home_runs >= 0" CHECK (home_runs >= 0),
    CONSTRAINT "ibb >= 0" CHECK (ibb >= 0),
    CONSTRAINT "obp >= 0" CHECK (obp >= 0::numeric),
    CONSTRAINT "ops >= 0" CHECK (ops >= 0::numeric),
    CONSTRAINT "plate_appearances >= 0" CHECK (plate_appearances >= 0),
    CONSTRAINT "rbis >= 0" CHECK (rbis >= 0),
    CONSTRAINT "runs >= 0" CHECK (runs >= 0),
    CONSTRAINT "sacrifice_fly >= 0" CHECK (sacrifice_fly >= 0),
    CONSTRAINT "slg >= 0" CHECK (slg >= 0::numeric),
    CONSTRAINT "stolen_bases >= 0" CHECK (stolen_bases >= 0),
    CONSTRAINT "strikeouts >= 0" CHECK (strikeouts >= 0),
    CONSTRAINT "total_bases >= 0" CHECK (total_bases >= 0),
    CONSTRAINT "triples >= 0" CHECK (triples >= 0),
    CONSTRAINT "walks >= 0" CHECK (walks >= 0)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."PlayerBatYearResult"
    OWNER to postgres;


-- Table: public.TeamBatYearResult

-- DROP TABLE IF EXISTS public."TeamBatYearResult";

CREATE TABLE IF NOT EXISTS public."TeamBatYearResult"
(
    team_bat_year_result_id serial NOT NULL,
    year integer NOT NULL,
    games integer DEFAULT 0,
    plate_appearances integer DEFAULT 0,
    at_bats integer DEFAULT 0,
    runs integer DEFAULT 0,
    hits integer DEFAULT 0,
    doubles integer DEFAULT 0,
    triples integer DEFAULT 0,
    home_runs integer DEFAULT 0,
    rbis integer DEFAULT 0,
    stolen_bases integer DEFAULT 0,
    caught_stealing integer DEFAULT 0,
    walks integer DEFAULT 0,
    strikeouts integer DEFAULT 0,
    batting_average numeric(3,3) DEFAULT 0,
    obp numeric(3,3) DEFAULT 0,
    slg numeric(3,3) DEFAULT 0,
    ops numeric(3,3) DEFAULT 0,
    ops_plus integer DEFAULT 0,
    total_bases integer DEFAULT 0,
    gdp integer DEFAULT 0,
    hbp integer DEFAULT 0,
    sacrifice_fly integer DEFAULT 0,
    ibb integer DEFAULT 0,
    CONSTRAINT "TeamBatYearResult_pkey" PRIMARY KEY (team_bat_year_result_id),
    CONSTRAINT "Unique_year_team_team_bat_year_stats" UNIQUE (year),
    CONSTRAINT "at_bats >= 0" CHECK (at_bats >= 0),
    CONSTRAINT "batting_average >= 0" CHECK (batting_average >= 0::numeric),
    CONSTRAINT "caught_stealing >= 0" CHECK (caught_stealing >= 0),
    CONSTRAINT "doubles >= 0" CHECK (doubles >= 0),
    CONSTRAINT "games >= 0" CHECK (games >= 0),
    CONSTRAINT "gdp >= 0" CHECK (gdp >= 0),
    CONSTRAINT "hbp >= 0" CHECK (hbp >= 0),
    CONSTRAINT "hits >= 0" CHECK (hits >= 0),
    CONSTRAINT "home_runs >= 0" CHECK (home_runs >= 0),
    CONSTRAINT "ibb >= 0" CHECK (ibb >= 0),
    CONSTRAINT "obp >= 0" CHECK (obp >= 0::numeric),
    CONSTRAINT "ops >= 0" CHECK (ops >= 0::numeric),
    CONSTRAINT "plate_appearances >= 0" CHECK (plate_appearances >= 0),
    CONSTRAINT "rbis >= 0" CHECK (rbis >= 0),
    CONSTRAINT "runs >= 0" CHECK (runs >= 0),
    CONSTRAINT "sacrifice_fly >= 0" CHECK (sacrifice_fly >= 0),
    CONSTRAINT "slg >= 0" CHECK (slg >= 0::numeric),
    CONSTRAINT "stolen_bases >= 0" CHECK (stolen_bases >= 0),
    CONSTRAINT "strikeouts >= 0" CHECK (strikeouts >= 0),
    CONSTRAINT "total_bases >= 0" CHECK (total_bases >= 0),
    CONSTRAINT "triples >= 0" CHECK (triples >= 0),
    CONSTRAINT "walks >= 0" CHECK (walks >= 0)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."TeamBatYearResult"
    OWNER to postgres;


-- Table: public.PlayerPitchYearResult

-- DROP TABLE IF EXISTS public."PlayerPitchYearResult";

CREATE TABLE IF NOT EXISTS public."PlayerPitchYearResult"
(
    player_pitch_year_result_id serial NOT NULL,
    year integer NOT NULL,
    player_id integer NOT NULL,
    wins integer NOT NULL DEFAULT 0,
    losses integer NOT NULL DEFAULT 0,
    win_percentage numeric(3,3) NOT NULL DEFAULT 0,
    era numeric(3,3) DEFAULT 0,
    games integer DEFAULT 0,
    games_started integer DEFAULT 0,
    games_finished integer DEFAULT 0,
    complete_games integer DEFAULT 0,
    shutouts integer DEFAULT 0,
    saves integer DEFAULT 0,
    innings_pitched numeric(4,1) DEFAULT 0,
    hits integer DEFAULT 0,
    runs integer DEFAULT 0,
    earned_runs integer DEFAULT 0,
    home_runs integer DEFAULT 0,
    walks integer DEFAULT 0,
    intentional_walks integer DEFAULT 0,
    strikeouts integer DEFAULT 0,
    hbp integer DEFAULT 0,
    balks integer DEFAULT 0,
    wild_pitches integer DEFAULT 0,
    batters_faced integer DEFAULT 0,
    era_plus numeric(3,3) DEFAULT 0,
    fip numeric(3,2) DEFAULT 0,
    whip numeric(4,3) DEFAULT 0,
    hits_per_9 numeric(4,2) DEFAULT 0,
    bb_per_9 numeric(4,2) DEFAULT 0,
    k_per_9 numeric(4,2) DEFAULT 0,
    CONSTRAINT player_pitch_year_result_pk PRIMARY KEY (player_pitch_year_result_id),
    CONSTRAINT "Unique_player_pitch_year_result" UNIQUE (year, player_id),
    CONSTRAINT player_pitch_year_result_player_fk FOREIGN KEY (player_id)
        REFERENCES public."Player" (player_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT "balks >= 0" CHECK (balks >= 0),
    CONSTRAINT "batters_faced >= 0" CHECK (batters_faced >= 0),
    CONSTRAINT "bb_per_9 >= 0" CHECK (bb_per_9 >= 0::numeric),
    CONSTRAINT "complete_games >= 0" CHECK (complete_games >= 0),
    CONSTRAINT "earned_runs >= 0" CHECK (earned_runs >= 0),
    CONSTRAINT "era >= 0" CHECK (era >= 0::numeric),
    CONSTRAINT "era_plus >= 0" CHECK (era_plus >= 0::numeric),
    CONSTRAINT "fip >= 0" CHECK (fip >= 0::numeric),
    CONSTRAINT "games >= 0" CHECK (games >= 0),
    CONSTRAINT "games_finished >= 0" CHECK (games_finished >= 0),
    CONSTRAINT "games_started >= 0" CHECK (games_started >= 0),
    CONSTRAINT "hbp >= 0" CHECK (hbp >= 0),
    CONSTRAINT "hits >= 0" CHECK (hits >= 0),
    CONSTRAINT "hits_per_9 >= 0" CHECK (hits_per_9 >= 0::numeric),
    CONSTRAINT "home_runs >= 0" CHECK (home_runs >= 0),
    CONSTRAINT "innings_pitched >= 0" CHECK (innings_pitched >= 0::numeric),
    CONSTRAINT "intentional_walks >= 0" CHECK (intentional_walks >= 0),
    CONSTRAINT "k_per_9 >= 0" CHECK (k_per_9 >= 0::numeric),
    CONSTRAINT "losses >= 0" CHECK (losses >= 0),
    CONSTRAINT "runs >= 0" CHECK (runs >= 0),
    CONSTRAINT "saves >= 0" CHECK (saves >= 0),
    CONSTRAINT "shutouts >= 0" CHECK (shutouts >= 0),
    CONSTRAINT "strikeouts >= 0" CHECK (strikeouts >= 0),
    CONSTRAINT "walks >= 0" CHECK (walks >= 0),
    CONSTRAINT "whip >= 0" CHECK (whip >= 0::numeric),
    CONSTRAINT "wild_pitches >= 0" CHECK (wild_pitches >= 0),
    CONSTRAINT "win_percentage >= 0" CHECK (win_percentage >= 0::numeric),
    CONSTRAINT "wins >= 0" CHECK (wins >= 0)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."PlayerPitchYearResult"
    OWNER to postgres;


-- Table: public.TeamPitchYearResult

-- DROP TABLE IF EXISTS public."TeamPitchYearResult";

CREATE TABLE IF NOT EXISTS public."TeamPitchYearResult"
(
    team_pitch_year_result_id serial NOT NULL,
    year integer NOT NULL,
    wins integer NOT NULL DEFAULT 0,
    losses integer NOT NULL DEFAULT 0,
    win_percentage numeric(3,3) NOT NULL DEFAULT 0,
    era numeric(3,3) DEFAULT 0,
    games integer DEFAULT 0,
    games_started integer DEFAULT 0,
    games_finished integer DEFAULT 0,
    complete_games integer DEFAULT 0,
    shutouts integer DEFAULT 0,
    saves integer DEFAULT 0,
    innings_pitched numeric(4,1) DEFAULT 0,
    hits integer DEFAULT 0,
    runs integer DEFAULT 0,
    earned_runs integer DEFAULT 0,
    home_runs integer DEFAULT 0,
    walks integer DEFAULT 0,
    intentional_walks integer DEFAULT 0,
    strikeouts integer DEFAULT 0,
    hbp integer DEFAULT 0,
    balks integer DEFAULT 0,
    wild_pitches integer DEFAULT 0,
    batters_faced integer DEFAULT 0,
    era_plus numeric(3,3) DEFAULT 0,
    fip numeric(3,2) DEFAULT 0,
    whip numeric(4,3) DEFAULT 0,
    hits_per_9 numeric(4,2) DEFAULT 0,
    bb_per_9 numeric(4,2) DEFAULT 0,
    k_per_9 numeric(4,2) DEFAULT 0,
    CONSTRAINT team_pitch_year_result_pk PRIMARY KEY (team_pitch_year_result_id),
    CONSTRAINT "Unique_team_pitch_year_result" UNIQUE (year),
    CONSTRAINT "balks >= 0" CHECK (balks >= 0),
    CONSTRAINT "batters_faced >= 0" CHECK (batters_faced >= 0),
    CONSTRAINT "bb_per_9 >= 0" CHECK (bb_per_9 >= 0::numeric),
    CONSTRAINT "complete_games >= 0" CHECK (complete_games >= 0),
    CONSTRAINT "earned_runs >= 0" CHECK (earned_runs >= 0),
    CONSTRAINT "era >= 0" CHECK (era >= 0::numeric),
    CONSTRAINT "era_plus >= 0" CHECK (era_plus >= 0::numeric),
    CONSTRAINT "fip >= 0" CHECK (fip >= 0::numeric),
    CONSTRAINT "games >= 0" CHECK (games >= 0),
    CONSTRAINT "games_finished >= 0" CHECK (games_finished >= 0),
    CONSTRAINT "games_started >= 0" CHECK (games_started >= 0),
    CONSTRAINT "hbp >= 0" CHECK (hbp >= 0),
    CONSTRAINT "hits >= 0" CHECK (hits >= 0),
    CONSTRAINT "hits_per_9 >= 0" CHECK (hits_per_9 >= 0::numeric),
    CONSTRAINT "home_runs >= 0" CHECK (home_runs >= 0),
    CONSTRAINT "innings_pitched >= 0" CHECK (innings_pitched >= 0::numeric),
    CONSTRAINT "intentional_walks >= 0" CHECK (intentional_walks >= 0),
    CONSTRAINT "k_per_9 >= 0" CHECK (k_per_9 >= 0::numeric),
    CONSTRAINT "losses >= 0" CHECK (losses >= 0),
    CONSTRAINT "runs >= 0" CHECK (runs >= 0),
    CONSTRAINT "saves >= 0" CHECK (saves >= 0),
    CONSTRAINT "shutouts >= 0" CHECK (shutouts >= 0),
    CONSTRAINT "strikeouts >= 0" CHECK (strikeouts >= 0),
    CONSTRAINT "walks >= 0" CHECK (walks >= 0),
    CONSTRAINT "whip >= 0" CHECK (whip >= 0::numeric),
    CONSTRAINT "wild_pitches >= 0" CHECK (wild_pitches >= 0),
    CONSTRAINT "win_percentage >= 0" CHECK (win_percentage >= 0::numeric),
    CONSTRAINT "wins >= 0" CHECK (wins >= 0)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."TeamPitchYearResult"
    OWNER to postgres;


-- Table: public.PlayerFieldYearResult

-- DROP TABLE IF EXISTS public."PlayerFieldYearResult";

CREATE TABLE IF NOT EXISTS public."PlayerFieldYearResult"
(
    player_field_year_result_id bigserial NOT NULL,
    year integer NOT NULL,
    player_id integer NOT NULL,
    games integer NOT NULL DEFAULT 0,
    games_started integer NOT NULL DEFAULT 0,
    innings numeric(4,1) DEFAULT 0,
    putouts integer DEFAULT 0,
    assists integer DEFAULT 0,
    errors integer DEFAULT 0,
    double_plays integer DEFAULT 0,
    fielding_percentage numeric(3,3) DEFAULT 0,
    drs numeric(3,1) DEFAULT 0,
    drs_per_year numeric(3,1) DEFAULT 0,
    CONSTRAINT "PlayerFieldYearResult_pkey" PRIMARY KEY (player_field_year_result_id),
    CONSTRAINT "Unique_player_field_year_result_player_year" UNIQUE (year, player_id),
    CONSTRAINT "Player_id_fk" FOREIGN KEY (player_id)
        REFERENCES public."Player" (player_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT "assists >= 0" CHECK (assists >= 0),
    CONSTRAINT "double_plays >= 0" CHECK (double_plays >= 0),
    CONSTRAINT "drs >= -50 and drs <= 50" CHECK (drs >= '-50'::integer::numeric AND drs <= 50::numeric),
    CONSTRAINT "drs_per_year >= -100 and drs <= 100" CHECK (drs_per_year >= '-100'::integer::numeric AND drs <= 100::numeric),
    CONSTRAINT "errors >= 0" CHECK (errors >= 0),
    CONSTRAINT "fielding_percentage >= 0" CHECK (fielding_percentage >= 0::numeric),
    CONSTRAINT "games >= 0" CHECK (games >= 0),
    CONSTRAINT "games_started >= 0" CHECK (games_started >= 0),
    CONSTRAINT "innings >= 0" CHECK (innings >= 0::numeric),
    CONSTRAINT "putouts >= 0" CHECK (putouts >= 0)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."PlayerFieldYearResult"
    OWNER to postgres;


-- Table: public.TeamFieldYearResult

-- DROP TABLE IF EXISTS public."TeamFieldYearResult";

CREATE TABLE IF NOT EXISTS public."TeamFieldYearResult"
(
    team_field_year_result_id serial NOT NULL,
    year integer NOT NULL,
    games integer NOT NULL DEFAULT 0,
    games_started integer NOT NULL DEFAULT 0,
    innings numeric(4,1) DEFAULT 0,
    putouts integer DEFAULT 0,
    assists integer DEFAULT 0,
    errors integer DEFAULT 0,
    double_plays integer DEFAULT 0,
    fielding_percentage numeric(3,3) DEFAULT 0,
    drs numeric(3,1) DEFAULT 0,
    drs_per_year numeric(3,1) DEFAULT 0,
    CONSTRAINT "TeamFieldYearResult_pkey" PRIMARY KEY (team_field_year_result_id),
    CONSTRAINT "Unique_team_field_year_result_year" UNIQUE (year),
    CONSTRAINT "assists >= 0" CHECK (assists >= 0),
    CONSTRAINT "double_plays >= 0" CHECK (double_plays >= 0),
    CONSTRAINT "drs >= -50 and drs <= 50" CHECK (drs >= '-50'::integer::numeric AND drs <= 50::numeric),
    CONSTRAINT "drs_per_year >= -100 and drs <= 100" CHECK (drs_per_year >= '-100'::integer::numeric AND drs <= 100::numeric),
    CONSTRAINT "errors >= 0" CHECK (errors >= 0),
    CONSTRAINT "fielding_percentage >= 0" CHECK (fielding_percentage >= 0::numeric),
    CONSTRAINT "games >= 0" CHECK (games >= 0),
    CONSTRAINT "games_started >= 0" CHECK (games_started >= 0),
    CONSTRAINT "innings >= 0" CHECK (innings >= 0::numeric),
    CONSTRAINT "putouts >= 0" CHECK (putouts >= 0)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."TeamFieldYearResult"
    OWNER to postgres;


-- Table: public.Game

-- DROP TABLE IF EXISTS public."Game";

CREATE TABLE IF NOT EXISTS public."Game"
(
    game_id bigserial NOT NULL,
    year integer NOT NULL,
    game_number integer NOT NULL,
    result character(1) NOT NULL,
    date date NOT NULL,
    month integer,
    opponent text COLLATE pg_catalog."default" NOT NULL,
    home_or_away text COLLATE pg_catalog."default" NOT NULL,
    innings integer NOT NULL DEFAULT 9,
    team_wins_after integer NOT NULL,
    team_losses_after integer NOT NULL,
    "time" time without time zone,
    attendance integer,
    winning_pitcher text COLLATE pg_catalog."default" NOT NULL,
    losing_pitcher text COLLATE pg_catalog."default" NOT NULL,
    saving_pitcher text COLLATE pg_catalog."default",
    CONSTRAINT "Game_pkey" PRIMARY KEY (game_id),
    CONSTRAINT "Unique_Game" UNIQUE (year, game_number, date),
    CONSTRAINT "year >= 1900" CHECK (year >= 1900),
    CONSTRAINT "game_number >= 1" CHECK (game_number >= 1),
    CONSTRAINT "month >= 1 && month <= 12" CHECK (month >= 1 AND month <= 12),
    CONSTRAINT "home_or_away = 'home' or home_or_away = 'away'" CHECK (home_or_away = 'home'::bpchar::text OR home_or_away = 'away'::bpchar::text),
    CONSTRAINT "innings >= 1 && innings <= 50" CHECK (innings >= 1 AND innings <= 50),
    CONSTRAINT "team_wins_after >= 0" CHECK (team_wins_after >= 0),
    CONSTRAINT "team_losses_after >= 0" CHECK (team_losses_after >= 0),
    CONSTRAINT "attendance >= 0" CHECK (attendance >= 0)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Game"
    OWNER to postgres;

CREATE INDEX IF NOT EXISTS idx_game_year_num ON public."Game" (year, game_number);


-- Table: public.PlayerBatGameStat

-- DROP TABLE IF EXISTS public."PlayerBatGameStat";

CREATE TABLE IF NOT EXISTS public."PlayerBatGameStat"
(
    player_bat_game_stat_id bigserial NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    at_bats integer DEFAULT 0,
    runs integer DEFAULT 0,
    hits integer DEFAULT 0,
    runs_batted_in integer DEFAULT 0,
    walks integer DEFAULT 0,
    strikeouts integer DEFAULT 0,
    plate_appearances integer DEFAULT 0,
    batting_average numeric(3,3) DEFAULT 0,
    obp numeric(3,3) DEFAULT 0,
    slg numeric(3,3) DEFAULT 0,
    ops numeric(4,3) DEFAULT 0,
    pitches_seen integer DEFAULT 0,
    CONSTRAINT "PlayerBatGameStat_pkey" PRIMARY KEY (player_bat_game_stat_id),
    CONSTRAINT "Unique_game_player" UNIQUE (game_id, player_id),
    CONSTRAINT "Game_id_fk" FOREIGN KEY (game_id)
        REFERENCES public."Game" (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT "Player_id_fk" FOREIGN KEY (player_id)
        REFERENCES public."Player" (player_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT "at_bats >= 0" CHECK (at_bats >= 0),
    CONSTRAINT "batting_average >= 0 && batting_average <= 1" CHECK (batting_average >= 0::numeric AND batting_average <= 1::numeric),
    CONSTRAINT "hits >= 0" CHECK (hits >= 0),
    CONSTRAINT "obp >= 0" CHECK (obp >= 0::numeric),
    CONSTRAINT "ops >= 0" CHECK (ops >= 0::numeric),
    CONSTRAINT "pitches_seen >= 0" CHECK (pitches_seen >= 0),
    CONSTRAINT "plate_appearances >= 0" CHECK (plate_appearances >= 0),
    CONSTRAINT "runs >= 0" CHECK (runs >= 0),
    CONSTRAINT "runs_batted_in >= 0" CHECK (runs_batted_in >= 0),
    CONSTRAINT "slg >= 0" CHECK (slg >= 0::numeric),
    CONSTRAINT "strikeouts >= 0" CHECK (strikeouts >= 0),
    CONSTRAINT "walks >= 0" CHECK (walks >= 0)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."PlayerBatGameStat"
    OWNER to postgres;


-- Table: public.TeamBatGameStat

-- DROP TABLE IF EXISTS public."TeamBatGameStat";

CREATE TABLE IF NOT EXISTS public."TeamBatGameStat"
(
    team_bat_game_stat_id serial NOT NULL,
    game_id integer NOT NULL,
    at_bats integer DEFAULT 0,
    runs integer DEFAULT 0,
    hits integer DEFAULT 0,
    runs_batted_in integer DEFAULT 0,
    walks integer DEFAULT 0,
    strikeouts integer DEFAULT 0,
    plate_appearances integer DEFAULT 0,
    batting_average numeric(3,3) DEFAULT 0,
    obp numeric(3,3) DEFAULT 0,
    slg numeric(3,3) DEFAULT 0,
    ops numeric(4,3) DEFAULT 0,
    pitches_seen integer DEFAULT 0,
    CONSTRAINT "TeamBatGameStat_pkey" PRIMARY KEY (team_bat_game_stat_id),
    CONSTRAINT "Unique_game" UNIQUE (game_id),
    CONSTRAINT "Game_id_fk" FOREIGN KEY (game_id)
        REFERENCES public."Game" (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT "at_bats >= 0" CHECK (at_bats >= 0),
    CONSTRAINT "batting_average >= 0 && batting_average <= 1" CHECK (batting_average >= 0::numeric AND batting_average <= 1::numeric),
    CONSTRAINT "hits >= 0" CHECK (hits >= 0),
    CONSTRAINT "obp >= 0" CHECK (obp >= 0::numeric),
    CONSTRAINT "ops >= 0" CHECK (ops >= 0::numeric),
    CONSTRAINT "pitches_seen >= 0" CHECK (pitches_seen >= 0),
    CONSTRAINT "plate_appearances >= 0" CHECK (plate_appearances >= 0),
    CONSTRAINT "runs >= 0" CHECK (runs >= 0),
    CONSTRAINT "runs_batted_in >= 0" CHECK (runs_batted_in >= 0),
    CONSTRAINT "slg >= 0" CHECK (slg >= 0::numeric),
    CONSTRAINT "strikeouts >= 0" CHECK (strikeouts >= 0),
    CONSTRAINT "walks >= 0" CHECK (walks >= 0)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."TeamBatGameStat"
    OWNER to postgres;


-- Table: public.PlayerPitchGameStat

-- DROP TABLE IF EXISTS public."PlayerPitchGameStat";

CREATE TABLE IF NOT EXISTS public."PlayerPitchGameStat"
(
    player_pitch_game_stat_id bigserial NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    innings_pitched numeric(4,1) DEFAULT 0,
    hits integer DEFAULT 0,
    runs integer DEFAULT 0,
    earned_runs integer DEFAULT 0,
    walks integer DEFAULT 0,
    strikeouts integer DEFAULT 0,
    home_runs integer DEFAULT 0,
    era numeric(6,3) DEFAULT 0,
    batters_faced integer DEFAULT 0,
    pitches integer DEFAULT 0,
    strikes integer DEFAULT 0,
    ground_balls integer DEFAULT 0,
    line_drives integer DEFAULT 0,
    fly_balls integer DEFAULT 0,
    CONSTRAINT "PlayerPitchGameStat_pkey" PRIMARY KEY (player_pitch_game_stat_id),
    CONSTRAINT "Unique_player_pitch_game_stat_game_player" UNIQUE (game_id, player_id),
    CONSTRAINT "Game_id_fk" FOREIGN KEY (game_id)
        REFERENCES public."Game" (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT "Player_id_fk" FOREIGN KEY (player_id)
        REFERENCES public."Player" (player_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT "batters_faced >= 0" CHECK (batters_faced >= 0),
    CONSTRAINT "earned_runs >= 0" CHECK (earned_runs >= 0),
    CONSTRAINT "era >= 0" CHECK (era >= 0::numeric),
    CONSTRAINT "fly_balls >= 0" CHECK (fly_balls >= 0),
    CONSTRAINT "ground_balls >= 0" CHECK (ground_balls >= 0),
    CONSTRAINT "hits >= 0" CHECK (hits >= 0),
    CONSTRAINT "home_runs >= 0" CHECK (home_runs >= 0),
    CONSTRAINT "innings_pitched >= 0" CHECK (innings_pitched >= 0::numeric),
    CONSTRAINT "line_drives >= 0" CHECK (line_drives >= 0),
    CONSTRAINT "pitches >= 0" CHECK (pitches >= 0),
    CONSTRAINT "runs >= 0" CHECK (runs >= 0),
    CONSTRAINT "strikeouts >= 0" CHECK (strikeouts >= 0),
    CONSTRAINT "strikes >= 0" CHECK (strikes >= 0),
    CONSTRAINT "walks >= 0" CHECK (walks >= 0)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."PlayerPitchGameStat"
    OWNER to postgres;


-- Table: public.TeamPitchGameStat

-- DROP TABLE IF EXISTS public."TeamPitchGameStat";

CREATE TABLE IF NOT EXISTS public."TeamPitchGameStat"
(
    team_pitch_game_stat_id serial NOT NULL,
    game_id integer NOT NULL,
    innings_pitched numeric(4,1) DEFAULT 0,
    hits integer DEFAULT 0,
    runs integer DEFAULT 0,
    earned_runs integer DEFAULT 0,
    walks integer DEFAULT 0,
    strikeouts integer DEFAULT 0,
    home_runs integer DEFAULT 0,
    era numeric(6,3) DEFAULT 0,
    batters_faced integer DEFAULT 0,
    pitches integer DEFAULT 0,
    strikes integer DEFAULT 0,
    ground_balls integer DEFAULT 0,
    line_drives integer DEFAULT 0,
    fly_balls integer DEFAULT 0,
    CONSTRAINT "TeamPitchGameStat_pkey" PRIMARY KEY (team_pitch_game_stat_id),
    CONSTRAINT "Unique_team_pitch_game_stat_game" UNIQUE (game_id),
    CONSTRAINT "Game_id_fk" FOREIGN KEY (game_id)
        REFERENCES public."Game" (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT "batters_faced >= 0" CHECK (batters_faced >= 0),
    CONSTRAINT "earned_runs >= 0" CHECK (earned_runs >= 0),
    CONSTRAINT "era >= 0" CHECK (era >= 0::numeric),
    CONSTRAINT "fly_balls >= 0" CHECK (fly_balls >= 0),
    CONSTRAINT "ground_balls >= 0" CHECK (ground_balls >= 0),
    CONSTRAINT "hits >= 0" CHECK (hits >= 0),
    CONSTRAINT "home_runs >= 0" CHECK (home_runs >= 0),
    CONSTRAINT "innings_pitched >= 0" CHECK (innings_pitched >= 0::numeric),
    CONSTRAINT "line_drives >= 0" CHECK (line_drives >= 0),
    CONSTRAINT "pitches >= 0" CHECK (pitches >= 0),
    CONSTRAINT "runs >= 0" CHECK (runs >= 0),
    CONSTRAINT "strikeouts >= 0" CHECK (strikeouts >= 0),
    CONSTRAINT "strikes >= 0" CHECK (strikes >= 0),
    CONSTRAINT "walks >= 0" CHECK (walks >= 0)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."TeamPitchGameStat"
    OWNER to postgres;


-- Table: public.TeamManagement

-- DROP TABLE IF EXISTS public."TeamManagement";

CREATE TABLE IF NOT EXISTS public."TeamManagement"
(
    team_management_id serial NOT NULL,
    year integer NOT NULL,
    manager text COLLATE pg_catalog."default" NOT NULL,
    general_manager text COLLATE pg_catalog."default" NOT NULL,
    president text COLLATE pg_catalog."default",
    CONSTRAINT "TeamManagement_pkey" PRIMARY KEY (team_management_id),
    CONSTRAINT "Unique_year_manager_gm_president" UNIQUE (year, manager, general_manager, president),
    CONSTRAINT "year >= 1900" CHECK (year >= 1900)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."TeamManagement"
    OWNER to postgres;


-- Table: public.TeamCoach

-- DROP TABLE IF EXISTS public."TeamCoach";

CREATE TABLE IF NOT EXISTS public."TeamCoach"
(
    team_coach_id serial NOT NULL,
    year integer NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    coach_type text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "TeamCoach_pkey" PRIMARY KEY (team_coach_id),
    CONSTRAINT "Unique_team_coach_year_name" UNIQUE (year, name),
    CONSTRAINT "year >= 1900" CHECK (year >= 1900)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."TeamCoach"
    OWNER to postgres;


-- Table: public.TeamYearSplit

-- DROP TABLE IF EXISTS public."TeamYearSplit";

CREATE TABLE IF NOT EXISTS public."TeamYearSplit"
(
    team_year_split_id serial NOT NULL,
    year integer NOT NULL,
    home_or_away character varying(4) COLLATE pg_catalog."default" NOT NULL DEFAULT 'home'::character varying,
    runs_scored integer NOT NULL DEFAULT 0,
    runs_allowed integer NOT NULL DEFAULT 0,
    CONSTRAINT "TeamYearSplit_pkey" PRIMARY KEY (team_year_split_id),
    CONSTRAINT "Unique_team_year_split_year_home_or_away" UNIQUE (year, home_or_away),
    CONSTRAINT "home_or_away = 'home' or home_or_away = 'away'" CHECK (home_or_away::text = 'home'::text OR home_or_away::text = 'away'::text),
    CONSTRAINT "runs_allowed >= 0" CHECK (runs_allowed >= 0),
    CONSTRAINT "runs_scored >= 0" CHECK (runs_scored >= 0),
    CONSTRAINT "year >= 1900" CHECK (year >= 1900)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."TeamYearSplit"
    OWNER to postgres;


-- Table: public.TeamResult

-- DROP TABLE IF EXISTS public."TeamResult";

CREATE TABLE IF NOT EXISTS public."TeamResult"
(
    team_result_id serial NOT NULL,
    year integer NOT NULL,
    wins integer NOT NULL DEFAULT 0,
    losses integer NOT NULL DEFAULT 0,
    ties integer DEFAULT 0,
    division_place integer,
    attendance integer DEFAULT 0,
    CONSTRAINT "TeamResult_pkey" PRIMARY KEY (team_result_id),
    CONSTRAINT "Unique_team_result_year" UNIQUE (year),
    CONSTRAINT "attendance >= 0" CHECK (attendance >= 0),
    CONSTRAINT "division_place >= 1 and division_place <= 10" CHECK (division_place >= 1 AND division_place <= 10),
    CONSTRAINT "losses >= 0" CHECK (losses >= 0),
    CONSTRAINT "ties >= 0" CHECK (ties >= 0),
    CONSTRAINT "wins >= 0" CHECK (wins >= 0),
    CONSTRAINT "year >= 1900" CHECK (year >= 1900)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."TeamResult"
    OWNER to postgres;


-- Table: public.TeamPostseasonResult

-- DROP TABLE IF EXISTS public."TeamPostseasonResult";

CREATE TABLE IF NOT EXISTS public."TeamPostseasonResult"
(
    team_postseason_result_id serial NOT NULL,
    team_result_id integer NOT NULL,
    series_name text COLLATE pg_catalog."default" NOT NULL,
    opponent text COLLATE pg_catalog."default" NOT NULL,
    result text COLLATE pg_catalog."default" NOT NULL DEFAULT 'win'::text,
    CONSTRAINT "TeamPostseasonResult_pkey" PRIMARY KEY (team_postseason_result_id),
    CONSTRAINT "Player_id_fk" FOREIGN KEY (team_result_id)
        REFERENCES public."TeamResult" (team_result_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT "Unique_postseason_result_year_series_name" UNIQUE (team_result_id, series_name),
    CONSTRAINT "result = 'win' or result = 'loss'" CHECK (result = 'win'::text OR result = 'loss'::text)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."TeamPostseasonResult"
    OWNER to postgres;