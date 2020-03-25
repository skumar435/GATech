import http.client
import json
import time
import sys
import collections

conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"

def getPopMovies(api_key, genre_id, date):
	page_results = []
	movie_list = []
	movie_list_for_ref = {}
	for page in range(1,19):
		conn.request("GET", "/3/discover/movie?with_genres={}&primary_release_date.gte={}&page={}&include_video=false&include_adult=false&sort_by=popularity.desc&api_key={}".format(genre_id, date, str(page), api_key), payload)
		res = conn.getresponse()
		data = res.read()
		page_results = json.loads(data)
		for movie in page_results["results"]:
			if len(movie_list) < 350:
				movie_list.append("{},{}\n".format(movie["id"], movie["original_title"]))
				movie_list_for_ref[movie["id"]] = movie["original_title"]
	return movie_list, movie_list_for_ref

def getSimMovies(api_key, movie_id):
	conn.request("GET", "/3/movie/{}/similar?page=1&api_key={}".format(movie_id, api_key), payload)
	res = conn.getresponse()
	data = res.read()
	page_results = json.loads(data)
	sim_movie_list = []
	if len(page_results["results"]) > 0:
		if len(page_results["results"]) > 5:
			i = 0
			while i < 5:
				sim_movie_list.append(page_results["results"][i]["id"])
				i += 1
		else:
			for movie_id in page_results["results"]:
				sim_movie_list.append(movie_id["id"])
	return sim_movie_list

def write_to_file(fname, content):
	with open(fname, 'w') as fh:
		fh.writelines(content)

def main():
	api_key = sys.argv[1]
	genre_id = "18"
	date = "2004-01-01"
	out_file1 = "movie_ID_name.csv"
	out_file2 = "movie_ID_sim_movie_ID.csv"
	movie_list_content = []
	movie_dict = {}
	movie_list_content, movie_dict = getPopMovies(api_key, genre_id, date)
	write_to_file(out_file1, movie_list_content)
	sim_movie_dict = {}
	sim_mv_content = []
	for movie in movie_dict:
		time.sleep(0.4)
		sim_movie_lst = getSimMovies(api_key, movie)
		if len(sim_movie_lst) > 0:
			for mv in sim_movie_lst:
				if mv in sim_movie_dict:
					if movie in sim_movie_dict[mv]:
						sim_movie_lst.remove(mv)
					else:
						sim_mv_content.append("{},{}\n".format(movie, mv))
				else:
					sim_mv_content.append("{},{}\n".format(movie, mv))
			if len(sim_movie_lst) > 0:
				sim_movie_dict[movie] = sim_movie_lst
	write_to_file(out_file2, sim_mv_content)

main()