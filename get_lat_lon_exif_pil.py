from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image):
    """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]
                    #print t, sub_decoded, value[t]
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value

    return exif_data


def _get_if_exist(data, key):
    if key in data:
        return data[key]

    return None


def _convert_to_degress(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)


def get_lat_lon(exif_data):
    """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
    dir = None
    lat = None
    lon = None

    if "GPSInfo" in exif_data:
        gps_info = exif_data["GPSInfo"]

        gps_direction = _get_if_exist(gps_info, 'GPSImgDirection')
        gps_direction_ref = _get_if_exist(gps_info, 'GPSImgDirectionRef')
        gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = _get_if_exist(gps_info, 'GPSLatitudeRef')
        gps_longitude = _get_if_exist(gps_info, 'GPSLongitude')
        gps_longitude_ref = _get_if_exist(gps_info, 'GPSLongitudeRef')

        #print gps_direction, gps_direction_ref
        #print gps_latitude, gps_latitude_ref
        #print gps_longitude, gps_longitude_ref
        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            if gps_direction_ref and gps_direction:
                dir = _convert_to_degress(gps_direction)
                if gps_direction_ref != "N":
                    dir = 0 - dir
            else:
                dir = None

            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":
                lat = 0 - lat

            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon


    return dir, lat, lon


################
# Example ######
################
if __name__ == "__main__":
    image = Image.open("/Users/bound_to_love/Downloads/Waipuna_90m.JPG")  # load an image through PIL's Image object
    exif_data = get_exif_data(image)
    print (get_lat_lon(exif_data))