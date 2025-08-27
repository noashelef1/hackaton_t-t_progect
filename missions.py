def research_filter(missions_details_dict, users_filter_dict):
    missions_filtered_list = []

    for mission in missions_details_dict:
        for details in mission:
            if details in users_filter_dict.keys() and mission not in missions_filtered_list:
                missions_filtered_list.append(mission)

    return missions_filtered_list