#!/usr/bin/python

import sys
import random
import commands

lorem = "Phasellus convallis pretium magna. Etiam velit purus, euismod et risus vitae, consequat mollis sem. Fusce blandit hendrerit ligula, in pulvinar dolor condimentum sed. Donec nec elit vitae velit ultricies faucibus in at felis. Aenean non tempor lectus. Praesent in nisi eu sapien viverra dapibus. Ut eleifend quam orci, auctor luctus massa dignissim vel. Etiam lacinia eleifend fringilla. Maecenas eu sapien non neque ullamcorper pulvinar. Quisque at sapien nec lacus sodales eleifend non id eros. Mauris in augue eros. Sed a lacinia orci. Sed molestie placerat lorem, quis efficitur nisl pulvinar at. Morbi eu risus nec dolor convallis maximus. Nunc posuere, nulla a tincidunt vehicula, ante tellus ultrices est, quis sodales mauris justo ut lectus. Suspendisse a pulvinar odio, in ultrices ex."

colors = [ commands.getoutput("tput setaf %d" % i) for i in range(1,7) ]
bright = [ commands.getoutput("tput setaf %d" % i) for i in range(9,15) ]

count = 0
for sentence in [s.strip() for s in lorem.split(".") if s]:
    c = colors[count % len(colors)]
    b = bright[count % len(colors)]
    count += 1
    
    sys.stdout.write("%s" % c)
    words = sentence.split(" ")
    i = random.randint(0, len(words)-1)
    words[i] = "%s%s%s" % (b, words[i], c)
    sys.stdout.write("%s. " % (" ".join(words)))

print commands.getoutput("tput sgr0")
