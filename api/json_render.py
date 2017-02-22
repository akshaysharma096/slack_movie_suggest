def json_for_random_movie(data):
    response, attachments, genre, runtime, rating = {}, [], dict(), dict(), dict()
    synopsis, movie_info, year, fields = dict(), dict(), dict(), list()
    response['response_type'] = 'ephemeral'
    synopsis['title'], synopsis['text'] = 'Synopsis :spiral_note_pad:', data['synopsis']
    movie_info['title'], movie_info['image_url'] = '%s :clapper:' % data['title'], data['images']['poster']
    movie_info['title_link'] = "http://www.imdb.com/title/%s" % data['imdb_id']
    # ---Fields---
    year['title'], year['value'], year['short'] = "Year", data['year'], True
    genre['title'], genre['value'], genre['short'] = 'Genre', ', '.join([x.title() for x in data['genres']]), True
    runtime['title'], runtime['value'], runtime['short'] = 'Runtime', '%s minutes' % data['runtime'], True
    rating['title'], rating['value'], rating['short'] = 'IMDb rating', data['rating']['percentage'] /10, True
    fields.append(year), fields.append(genre), fields.append(runtime), fields.append(rating)
    if data['certification']:
        certification = dict()
        certification['title'], certification['value'], certification['short'] = 'Certification', data[
            'certification'], True
        fields.append(certification)
    # --Fields end---
    movie_info['fields'] = fields
    if data['trailer']:
        response['text'], response['unfurl_links'] = data['trailer'], True
        attachments.append(synopsis), attachments.append(movie_info)
    else:
        attachments.append(movie_info), attachments.append(synopsis)
    response['attachments'] = attachments
    return response
