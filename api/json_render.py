from api.epoch import get_epoch


def json_for_random_movie(data):
    response, attachments, genre, runtime = {}, [], dict(), dict()
    synopsis, movie_info, year, fields = dict(), dict(), dict(), list()
    response['text'] = 'Another movie :the_horns:'
    synopsis['title'], synopsis['text'], synopsis['color'] = 'Synopsis', data['synopsis'], '#36a64f'
    synopsis['ts'] = get_epoch()
    movie_info['title'], movie_info['image_url'] = data['title'], data['images']['poster']
    movie_info['title_link'], movie_info['color'] = "http://www.imdb.com/title/%s" % data['imdb_id'], '#36a64f'
    # ---Fields---
    year['title'], year['value'], year['short'] = "Year", data['year'], False
    genre['title'], genre['value'], genre['short'] = 'Genre', ', '.join([x.title() for x in data['genres']]), False
    runtime['title'], runtime['value'], runtime['short'] = 'Runtime', '%s minutes' % data['runtime'], False
    fields.append(year), fields.append(genre), fields.append(runtime)
    # --Fields end---
    movie_info['fields'] = fields
    attachments.append(movie_info), attachments.append(synopsis)
    response['attachments'] = attachments
    return response
