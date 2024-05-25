import pandas as pd
from csv_to_dataframe import csv_to_dataframe

#Funtions to clean each dataframe separately and store them in CSV.
def age_cleaned_to_csv(age_df):
    age_df.reset_index(drop=True, inplace=True)
    age_df.to_csv('NIBRS_age.csv')
    print('Cleaned age')

def arrestee_cleaned_to_csv(arrestee_df):
    arrestee_df.reset_index(drop=True, inplace=True)
    arrestee_df.drop(columns=['arrestee_seq_num','multiple_indicator','under_18_disposition_code','clearance_ind','age_range_low_num','age_range_high_num'],inplace=True)
    arrestee_df.to_csv('NIBRS_arrestee.csv')
    print('Cleaned arrestee')

def arrest_type_cleaned_to_csv(arrest_type_df):
    arrest_type_df.reset_index(drop=True, inplace=True)
    arrest_type_df.to_csv('NIBRS_arrest_type.csv')
    print('Cleaned arrest_type')

def arrestee_weapon_cleaned_to_csv(arrestee_weapons_df):
    arrestee_weapons_df.reset_index(drop=True, inplace=True)
    arrestee_weapons_df = arrestee_weapons_df.drop(columns=['nibrs_arrestee_weapon_id'])
    arrestee_weapons_df.to_csv('NIBRS_arrestee_weapons.csv')

def criminal_act_cleaned_to_csv(criminal_act_df):
    criminal_act_df.reset_index(drop=True,inplace=True)
    criminal_act_df.to_csv('NIBRS_criminal_act.csv')
    print('Cleaned criminal act')

def criminal_act_type_cleaned_to_csv(criminal_act_type):
    criminal_act_type.reset_index(drop=True,inplace=True)
    criminal_act_type.to_csv('NIBRS_criminal_act_type.csv')
    print('Cleaned criminal act type')

def ethnicity_cleaned_to_csv(ethnicity_df):
    ethnicity_df.reset_index(drop=True, inplace=True)
    ethnicity_df.to_csv('NIBRS_ethnicity.csv')
    print('Cleaned ethnicity')

def incident_cleaned_to_csv(incident_df):
    incident_df.reset_index(drop=True, inplace=True)
    incident_df.drop(columns = ['agency_id','nibrs_month_id', 'cleared_except_id','cleared_except_date','data_home','orig_format','did'], inplace = True)
    incident_df = incident_df.dropna()
    incident_df.to_csv('NIBRS_incident.csv')
    print('Cleaned incident')

def injury_cleaned_to_csv(injury_cleaned_df):
    injury_cleaned_df.reset_index(drop=True, inplace=True)
    injury_cleaned_df.to_csv('NIBRS_injury.csv')
    print('Cleaned injury')

def location_type_cleaned_to_csv(location_type_df):
    location_type_df.reset_index(drop=True, inplace=True)
    location_type_df.to_csv('NIBRS_location_type.csv')
    print('Cleaned location type')

def offender_cleaned_to_csv(offender_cleaned_df):
    offender_cleaned_df.reset_index(drop=True, inplace=True)
    offender_cleaned_df.drop(columns=['offender_seq_num','age_range_low_num','age_range_high_num'],inplace=True)
    offender_cleaned_df = offender_cleaned_df.dropna()
    offender_cleaned_df.to_csv('NIBRS_offender.csv')
    print('Cleaned offender')


def offense_cleaned_to_csv(offense_cleaned_df):
    offense_cleaned_df.reset_index(drop=True, inplace=True)
    offense_cleaned_df.drop(columns=['num_premises_entered','method_entry_code'],inplace = True)
    offense_cleaned_df.to_csv('NIBRS_offense.csv')
    print('Cleaned offense')

def offense_type_cleaned_to_csv(offense_type_cleaned_df):
    offense_type_cleaned_df.reset_index(drop=True,inplace=True)
    offense_type_cleaned_df.drop(columns=['ct_flag','hc_flag','hc_code','offense_group'],inplace = True)
    offense_type_cleaned_df.to_csv('NIBRS_offense_type.csv')
    print('Cleaned offense type')


def relationship_cleaned_to_csv(relationship_cleaned_df):
    relationship_cleaned_df.reset_index(drop=True, inplace=True)
    relationship_cleaned_df.to_csv('NIBRS_relationship.csv')
    print('Cleaned relationship')

def victims_cleaned_to_csv(victim_df):
    victim_df.reset_index(drop=True, inplace=True)
    victim_df.drop(columns=['victim_seq_num','assignment_type_id','activity_type_id','outside_agency_id','age_range_low_num','age_code_range_high'], inplace = True)
    victim_df.dropna(inplace=True)
    victim_df.to_csv('NIBRS_victims.csv')
    print('Cleaned victims')

def victims_injury_cleaned_to_csv(victims_injury_df):
    victims_injury_df.reset_index(drop=True,inplace=True)
    victims_injury_df.to_csv('NIBRS_victims_injury.csv')
    print('Cleaned victim injury')

def victim_offender_relation_cleaned_to_csv(victim_offender_relation_df):
    victim_offender_relation_df.reset_index(drop=True, inplace=True)
    victim_offender_relation_df.drop(columns=['nibrs_victim_offender_id'],inplace=True)
    victim_offender_relation_df.to_csv('NIBRS_victim_offender_relation.csv')
    print('Cleaned victim offender relation')


def victim_offense_cleaned_to_csv(victim_offense_df):
    victim_offense_df.reset_index(drop=True,inplace=True)
    victim_offense_df.to_csv('NIBRS_victim_offense.csv')
    print('Cleaned victim offense')


def victim_type_cleaned_to_csv(victim_type_df):
    victim_type_df.reset_index(drop=True, inplace=True)
    victim_type_df.to_csv('NIBRS_victim_types.csv')
    print('Cleaned victim type')

def weapon_cleaned_to_csv(weapon_df):
    weapon_df.reset_index(drop=True, inplace=True)
    weapon_df = weapon_df.drop(columns=['nibrs_weapon_id'])
    weapon_df.to_csv('NIBRS_weapons.csv')
    print('Cleaned weapons')

def weapon_type_cleaned_to_csv(weapon_type_df):
    weapon_type_df.reset_index(drop=True, inplace=True)
    weapon_type_df.to_csv('NIBRS_weapon_type.csv')
    print('Cleaned weapons type')

def race_cleaned_to_csv(race_df):
    race_df.reset_index(drop=True,inplace=True)
    race_df.drop(columns = ['start_year','end_year','notes'],inplace=True)
    race_df.to_csv('NIBRS_races.csv')
    print('Cleaned race')

#function to combine dataframes stored in the list
def combine_dfs(df_list):
    combined_df = pd.DataFrame()
    for df in df_list:
        df.columns = df.columns.str.lower()
        combined_df = pd.concat([combined_df, df])
        combined_df.drop_duplicates(inplace=True)
    return combined_df

def main_func():
    #call function to retrieve the Dictionery of List of Data Frames
    dataframe_dict = csv_to_dataframe()

    #Combine dataframes
    for df_name,df_list in dataframe_dict.items():
        if df_name == 'NIBRS_AGE':
            nibrs_age_combined_df = combine_dfs(df_list)
            age_cleaned_to_csv(nibrs_age_combined_df)

        elif df_name == 'NIBRS_ARRESTEE':
            combined_arrestee_df = combine_dfs(df_list)
            arrestee_cleaned_to_csv(combined_arrestee_df)

        elif df_name == 'NIBRS_ARRESTEE_WEAPON':
            combined_arrestee_weapons_df = combine_dfs(df_list)
            arrestee_weapon_cleaned_to_csv(combined_arrestee_weapons_df)


        elif df_name == 'NIBRS_ARREST_TYPE':
            combined_arrest_type_df = combine_dfs(df_list)
            arrest_type_cleaned_to_csv(combined_arrest_type_df)

        elif df_name == 'NIBRS_CRIMINAL_ACT':
            combined_criminal_act_df = combine_dfs(df_list)
            criminal_act_cleaned_to_csv(combined_criminal_act_df)

        elif df_name == 'NIBRS_CRIMINAL_ACT_TYPE':
            combined_criminal_act_type_df = combine_dfs(df_list)
            criminal_act_type_cleaned_to_csv(combined_criminal_act_type_df)

        elif df_name == 'NIBRS_ETHNICITY':
            combined_ethnicity_df = combine_dfs(df_list)
            ethnicity_cleaned_to_csv(combined_ethnicity_df)

        elif df_name == 'NIBRS_incident':
            combined_incident_df = combine_dfs(df_list)
            incident_cleaned_to_csv(combined_incident_df)

        elif df_name == 'NIBRS_INJURY':
            combined_injury_df = combine_dfs(df_list)
            injury_cleaned_to_csv(combined_injury_df)

        elif df_name == 'NIBRS_LOCATION_TYPE':
            combined_location_type_df = combine_dfs(df_list)
            location_type_cleaned_to_csv(combined_location_type_df)

        elif df_name == 'NIBRS_OFFENDER':
            combined_offender_df = combine_dfs(df_list)
            offender_cleaned_to_csv(combined_offender_df)

        elif df_name == 'NIBRS_OFFENSE':
            combined_offense_df = combine_dfs(df_list)
            offense_cleaned_to_csv(combined_offense_df)

        elif df_name == 'NIBRS_OFFENSE_TYPE':
            combined_offense_type_df = combine_dfs(df_list)
            offense_type_cleaned_to_csv(combined_offense_type_df)


        elif df_name == 'NIBRS_RELATIONSHIP':
            combined_relation_df = combine_dfs(df_list)
            relationship_cleaned_to_csv(combined_relation_df)

        elif df_name == 'NIBRS_VICTIM':
            combined_victim_df = combine_dfs(df_list)
            victims_cleaned_to_csv(combined_victim_df)

        elif df_name == 'NIBRS_VICTIM_INJURY':
            combined_victim_injury_df = combine_dfs(df_list)
            victims_injury_cleaned_to_csv(combined_victim_injury_df)

        elif df_name == 'NIBRS_VICTIM_OFFENDER_REL':
            combined_victim_offender_relations_df = combine_dfs(df_list)
            victim_offender_relation_cleaned_to_csv(combined_victim_offender_relations_df)

        elif df_name == 'NIBRS_VICTIM_OFFENSE':
            combined_victim_offense_df = combine_dfs(df_list)
            victim_offense_cleaned_to_csv(combined_victim_offense_df)

        elif df_name == 'NIBRS_VICTIM_TYPE':
            combined_victim_type_df = combine_dfs(df_list)
            victim_type_cleaned_to_csv(combined_victim_type_df)

        elif df_name == 'NIBRS_WEAPON':
            combined_weapon_df =  combine_dfs(df_list)
            weapon_cleaned_to_csv(combined_weapon_df)

        elif df_name == 'NIBRS_WEAPON_TYPE':
            combined_weapon_type_df = combine_dfs(df_list)
            weapon_type_cleaned_to_csv(combined_weapon_type_df)

        elif df_name == 'REF_RACE':
            combined_race_cleaned_df = combine_dfs(df_list)
            race_cleaned_to_csv(combined_race_cleaned_df)

