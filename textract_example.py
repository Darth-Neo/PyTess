#! env python

__author__ = u'james.morris'

import os
import textract

import Logger
logger = Logger.setupLogging(__name__)
logger.setLevel(Logger.DEBUG)

if __name__ == u"__main__":
    numFilesParsed = 0
    subdir = u"testdata"
    # subdir = "/home/james.morris/Documents"

    listText = list()

    for root, dirs, files in os.walk(subdir, topdown=True):
        for name in files:
            nameFile = os.path.join(root, name)

            if nameFile[0] == u".":
                continue
            try:
                logger.debug(u"File : %s" % name)

                txt = textract.process(str(nameFile))
                t = txt.decode(u"utf8", errors=u"ignore")
                text = t.encode(u"ascii", errors=u"replace")

                logger.info(u"%d.%s - %s" % (len(text), nameFile, text[:20]))
                numFilesParsed += 1
                lt = list()
                lt.append(nameFile)
                lt.append(text)
                listText.append(lt)

            except Exception, msg:
                logger.error(u"%s [%20s]" % (nameFile, msg))

    for nameFile, text in listText:
        logger.info(u"%s : %s[%d]" % (nameFile, text[:30], len(text)))
