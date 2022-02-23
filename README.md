# Whale-and-Dolphin-Identification

We use fingerprints and facial recognition to identify people, but can we use similar approaches with animals? In fact, researchers manually track marine life by the shape and markings on their tails, dorsal fins, heads and other body parts. Identification by natural markings via photographs—known as photo-ID—is a powerful tool for marine mammal science. It allows individual animals to be tracked over time and enables assessments of population status and trends. With your help to automate whale and dolphin photo-ID, researchers can reduce image identification times by over 99%. More efficient identification could enable a scale of study previously unaffordable or impossible.

Currently, most research institutions rely on time-intensive—and sometimes inaccurate—manual matching by the human eye. Thousands of hours go into manual matching, which involves staring at photos to compare one individual to another, finding matches, and identifying new individuals. While researchers enjoy looking at a whale photo or two, manual matching limits the scope and reach.

Algorithms developed in this competition will be implemented in Happywhale, a research collaboration and citizen science web platform. Its mission is to increase global understanding and caring for marine environments through high quality conservation science and education. Happywhale aims to make it easy and rewarding for the public to participate in science by building innovative tools to engage anyone interested in marine mammals. The platform also serves the research community with powerful collaborative tools.

In this competition, you’ll develop a model to match individual whales and dolphins by unique—but often subtle—characteristics of their natural markings. You'll pay particular attention to dorsal fins and lateral body views in image sets from a multi-species dataset built by 28 research institutions. The best submissions will suggest photo-ID solutions that are fast and accurate.

If successful, you'll have a hand in building advanced technology to better understand and manage the impact on the world’s changing oceans. Previous automation attempts resulted in a global database of over 50,000 whales and an agreement with cruise ships to operate at a maximum speed of 11 mph in the most whale-rich region. Your ideas to automate the identification of marine life will help overcome increasing human impacts on oceans, providing a critical tool for conservation science. If there's a whale, there's a way!

https://www.kaggle.com/c/happy-whale-and-dolphin

############################################################################################################

To build project you need to have docker and docker-compose installed.

- To run project container in tensorflow cpu: 
    $ docker-compose --profile CPU up

- To run project container in tensorflow gpu:
    $ docker-compose --profile GPU up
