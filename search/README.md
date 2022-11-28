it is a search engine to search for images by a given key word and save in the background,
usage:

import search

S = search.Search(query, limit, output_dir, verbose)

query::key word
limit::number of images to search for
output_dir::name of the folder to save the images
verbose::print current state if true

//////////////////////////////////////////////////////

S.kill() to stop searching