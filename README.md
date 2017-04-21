# graphMyCommute

---

![oops](https://github.com/markhalonen/graphMyCommute/blob/master/Cool%20Charts/Commute_Duration_Heatmap.png)

## How-To

1. Clone this repo. `git clone https://github.com/markhalonen/graphMyCommute`
1. Hardest step. Get a google maps api key so you can request the travel time. Follow the steps in their [repo](https://github.com/googlemaps/google-maps-services-python)
2. Make a file `key.txt` a level up from the cloned repo and store your api key there.
3. Similarly, make `homeAddress.txt` and `workAddress.txt` in the parent directory.
4. Run `main.py`. This gets the data and stores it into a pickle file
5. Run `graphCommuteTime.py`. This loads the data and graphs it with the matplotlib library.
6. Make new charts and send me a pull request!

