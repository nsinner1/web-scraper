import pytest

from web_scraper.scraper import (get_citations_needed_count, get_citations_needed_report)

class TestScraper:
    report_1 = """Citation needed for Confusion over the state of Washington and the city of Washington, D.C., led to renaming proposals during the statehood process for Washington in 1889, including David Dudley Field II's suggestion to name the new state "Tacoma". These proposals failed to garner support.[10] Washington, D.C.'s, own statehood movement in the 21st century includes a proposal to use the name "State of Washington, Douglass Commonwealth", which would conflict with the current state of Washington.[11] Residents of Washington (known as "Washingtonians") and the Pacific Northwest simply refer to the state as "Washington", and the nation's capital "Washington, D.C.", "the other Washington",[12] or simply "D.C." 
Citation needed for Washington state has the 18th highest per capita effective tax rate in the United States, as of 2017. Their tax policy differs from neighboring Oregon's, which levies no sales tax, but does levy a personal income tax. This leads to border economic anomalies in the Portland-Vancouver metropolitan area.[112] Additional border economies exist with neighboring British Columbia and Idaho. 
Citation needed for Washington state has the 18th highest per capita effective tax rate in the United States, as of 2017. Their tax policy differs from neighboring Oregon's, which levies no sales tax, but does levy a personal income tax. This leads to border economic anomalies in the Portland-Vancouver metropolitan area.[112] Additional border economies exist with neighboring British Columbia and Idaho. 
Citation needed for There are extensive waterways around Washington's largest cities, including Seattle, Bellevue, Tacoma and Olympia. The state highways incorporate an extensive network of bridges and the largest ferry system in the United States to serve transportation needs in the Puget Sound area. Washington's marine highway constitutes a fleet of twenty-eight ferries that navigate Puget Sound and its inland waterways to 20 different ports of call, completing close to 147,000 sailings each year. Washington is home to four of the five longest floating bridges in the world: the Evergreen Point Floating Bridge, Lacey V. Murrow Memorial Bridge and Homer M. Hadley Memorial Bridge over Lake Washington, and the Hood Canal Bridge which connects the Olympic Peninsula and Kitsap Peninsula. Among its most famous bridges is the Tacoma Narrows Bridge, which collapsed in 1940 and was rebuilt. Washington has a number of seaports on the Pacific Ocean, including Seattle, Tacoma, Kalama, Anacortes, Vancouver, Longview, Grays Harbor, Olympia, and Port Angeles. 
Citation needed for The Cascade Mountain Range also impedes transportation. Washington operates and maintains roads over seven[vague] major mountain passes and eight minor passes. During winter months some of these passes are plowed, sanded, and kept safe with avalanche control. Not all stay open through the winter. The North Cascades Highway, State Route 20, closes every year due to snowfall and avalanches in the area of Washington Pass. The Cayuse and Chinook passes east of Mount Rainier also close in winter. 
Citation needed for Washington is crossed by a number of freight railroads, and Amtrak's passenger Cascade route between Eugene, Oregon and Vancouver, BC is the eighth busiest Amtrak service in the U.S. Seattle's King Street Station, the busiest station in Washington, and 15th busiest in the U.S.,[125] serves as the terminus for the two long distance Amtrak routes in Washington, the Empire Builder to Chicago and the Coast Starlight to Los Angeles. The Sounder commuter rail service operates in Seattle and its surrounding cities, between Everett and Lakewood. The intercity network includes the Cascade Tunnel, the longest railroad tunnel in the United States, which is part of the Stevens Pass route on the BNSF Northern Transcom. 
Citation needed for Sound Transit Link light rail currently operates in the Seattle area at a length of 20 miles (32 km), and in Tacoma at a length of 1.6 miles (2.6 km). The entire system has a funded expansion plan that will expand light rail to a total of 116 miles by 2041. Seattle also has a 3.8-mile (6.1 km) streetcar network with two lines and plans to expand further by 2025. Bus systems exist across the state, the busiest being King County Metro, located in Seattle and King County, with just above 122 million riders in 2017.[126] Residents of Vancouver have resisted proposals to extend Portland's mass transit system into Washington. 
"""


    report_2 = """Citation needed for Under earlier Spanish and Mexican rule, California's original native population had precipitously declined, above all, from Eurasian diseases to which the indigenous people of California had not yet developed a natural immunity.[67] Under its new American administration, California's harsh governmental policies towards its own indigenous people did not improve. As in other American states, many of the native inhabitants were soon forcibly removed from their lands by incoming American settlers such as miners, ranchers, and farmers. Although California had entered the American union as a free state, the "loitering or orphaned Indians" were de facto enslaved by their new Anglo-American masters under the 1853 Act for the Government and Protection of Indians.There were also massacres in which hundreds of indigenous people were killed.
Citation needed for Between 1850 and 1860, the California state government paid around 1.5 million dollars (some 250,000 of which was reimbursed by the federal government)[68] to hire militias whose purpose was to protect settlers from the indigenous populations. In later decades, the native population was placed in reservations and rancherias, which were often small and isolated and without enough natural resources or funding from the government to sustain the populations living on them. As a result, the rise of California was a calamity for the native inhabitants. Several scholars and Native American activists, including Benjamin Madley and Ed Castillo, have described the actions of the California government as a genocide.[69]
Citation needed for The Canadian zone mammals include the mountain weasel, snowshoe hare, and several species of chipmunks. Conspicuous birds include the blue-fronted jay, Sierra chickadee, Sierra hermit thrush, water ouzel, and Townsend's solitaire. As one ascends into the Hudsonian zone, birds become scarcer. While the Sierra rosy finch is the only bird native to the high Arctic region, other bird species such as the hummingbird and Clark's nutcracker. Principal mammals found in this region include the Sierra coney, white-tailed jackrabbit, and the bighorn sheep. As of April 2003, the bighorn sheep was listed as endangered by the U.S. Fish and Wildlife Service. The fauna found throughout several zones are the mule deer, coyote, mountain lion, northern flicker, and several species of hawk and sparrow.[105]
"""


    test_count = (
        ('https://en.wikipedia.org/wiki/Washington_(state)', 7),
        ('https://en.wikipedia.org/wiki/California', 3),
    )

    test_report = (
        ('https://en.wikipedia.org/wiki/Washington_(state)', report_1),
        ('https://en.wikipedia.org/wiki/California', report_2),
    )


    def test_proof_of_life(self):
        assert get_citations_needed_count
        assert get_citations_needed_report


    @pytest.mark.parametrize('url, _count', test_count)
    def test_citations_count(self, url, _count):
        assert get_citations_needed_count(url) == _count


    @pytest.mark.parametrize('url, report', test_report)
    def test_citations_report(self, url, report):
        assert get_citations_needed_report(url) == report
