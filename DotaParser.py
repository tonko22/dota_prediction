import numpy as np
import json
import dota2api

api = dota2api.Initialise("C9584BABBF2E4DD94346CBD112654677")
#Counts added strings to a txt file
get_counter = 0
add_counter = 0
copy_counter = 0

# hist = api.get_match_history(skill=3, min_players=10)
# hist = api.get_match_history_by_seq_num(start_at_match_seq_num=2769979621)


# Run script 100 times

for x in range(100):
    hist = api.get_match_history(skill=3, min_players=10)
    parsed_hist = json.loads(hist.json)

    for match in parsed_hist['matches']:
        seq_num = str(match['match_seq_num'])
        seq_hist = api.get_match_history_by_seq_num(start_at_match_seq_num=seq_num)
        parsed_seq = json.loads(seq_hist.json)
        for each in parsed_seq['matches']:
            current_match_id = int(each["match_id"])
            copy_counter = 0
            with open('DOTA_parsed.txt', 'r') as f:
                for line in f:
                    items = line.split(',')
                    #string to int
                    match_id_in_file = int(items[0])
                    if current_match_id == match_id_in_file:
                        copy_counter = copy_counter+1
                        print('Copy of  ', match_id_in_file)
                        break

            #Get Match Details
            if copy_counter == 0:
                current_match = api.get_match_details(match_id=current_match_id)
                print(current_match.url)
                parsed_match = json.loads(current_match.json)

                #Check leaver status
                def check_for_leavers():
                    for i in parsed_match["players"]:
                        if i["account_id"]:
                            if i["leaver_status"] > 0:
                                return False
                            return True
                        else:
                            return False


                print("ID", parsed_match["match_id"])
                print("REGION", parsed_match["cluster"])
                print("DURATION", parsed_match["duration"], check_for_leavers())
                print("______________")
                get_counter = get_counter +1
                    # 15min duration + no leavers
                if ((parsed_match["duration"] > 900) and (check_for_leavers()) and (parsed_match["game_mode"] == 2)):
                    # [match_id, game_mode, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, radiant_win, duration, cluster, lobby type]
                    result = np.array([
                        parsed_match["match_id"],
                        parsed_match["game_mode"],
                        parsed_match["players"][0]["hero_id"],
                        parsed_match["players"][1]["hero_id"],
                        parsed_match["players"][2]["hero_id"],
                        parsed_match["players"][3]["hero_id"],
                        parsed_match["players"][4]["hero_id"],
                        parsed_match["players"][5]["hero_id"],
                        parsed_match["players"][6]["hero_id"],
                        parsed_match["players"][7]["hero_id"],
                        parsed_match["players"][8]["hero_id"],
                        parsed_match["players"][9]["hero_id"],
                        parsed_match["radiant_win"],
                        parsed_match["duration"],
                        parsed_match["cluster"],
                        parsed_match["lobby_type"],
                        parsed_match["start_time"]
                        ])

                    #Append array to file
                    with open('DOTA_parsed.txt', 'ab') as file:
                        np.savetxt(file, result[np.newaxis], fmt='%i,')
                        add_counter = add_counter+1
                        print('{0} ADDED {1}, gm {2}'.format(match["match_id"], add_counter, parsed_match["game_mode"]))
        #time.sleep(60)

    print('ZAVERSHENO EPTA', get_counter)

#"""