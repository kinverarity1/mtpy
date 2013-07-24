try:
    import cStringIO as StringIO
except:
    import StringIO
import os
import urllib2
import zipfile


def download_coprod2_corrected(download_always=False):
    path = os.path.join('edis', 'coprod2_corrected')
    if not os.path.isdir(path) or download_always:
        uri = 'http://mtnet.dias.ie/data/coprod2/coprod2_edi.zip'
        zip = StringIO.StringIO(urllib2.urlopen(uri).read())
        z = zipfile.ZipFile(zip, mode='r')
        print('Downloaded %s' % uri)
        z.extractall(os.path.join('edis', 'coprod2_corrected'))
        print('Extracted files to %s' % path)
    else:
        print('Already downloaded at %s' % path)