#Iching Full Code 2023-10-22
import random
import urllib.parse
import webbrowser
from datetime import datetime
from pathlib import Path

question = str(input("What is your question? "))

sixth = random.randint(6,9)
fifth = random.randint(6,9)
fourth = random.randint(6,9)
third = random.randint(6,9)
second = random.randint(6,9)
first = random.randint(6,9)

zbior = [sixth, fifth, fourth, third, second, first]

def hex0(zbior):
    for linie in zbior:
        if linie == 9:
            print("_o_")
        elif linie == 8:
            print("---")
        elif linie == 7:
            print("___")
        elif linie == 6:
            print("-x-")
        else:
            print("error")

def hex1(zbior):
    for linie in zbior:
        if linie == 9:
            print("___")
        elif linie == 8:
            print("---")
        elif linie == 7:
            print("___")
        elif linie == 6:
            print("---")
        else:
            print("error")

def hex2(zbior):
    for linie in zbior:
        if linie == 9:
            print("---")
        elif linie == 8:
            print("---")
        elif linie == 7:
            print("___")
        elif linie == 6:
            print("___")
        else:
            print("error")

def change_line(zbior):
    for linie in zbior:
        if 6<linie<9:
            print(f"_no_change_")
        else:
            print(linie)

def print_changed_lines(lines):
    line_names = ["sixth", "fifth", "fourth", "third", "second", "first"]

    for i, value in enumerate(lines):
        if value in [6, 9]:
            print(f"-{line_names[i]} is changed")

lines = [sixth, fifth, fourth, third, second, first]

def convert_value(value):
    if value == 6:
        return 8
    elif value == 7:
        return 9
    elif value == 8:
        return 8
    elif value == 9:
        return 9
    else:
        return value

sixther = convert_value(sixth)
fifther = convert_value(fifth)
fourther = convert_value(fourth)
thirder = convert_value(third)
seconder = convert_value(second)
firster = convert_value(first)


def find_hex(sixther, fifther, fourther, thirder, seconder, firster):
    hexagram_data = [
        ("hex 1", 9, 9, 9, 9, 9, 9),
        ("hex 2", 8, 8, 8, 8, 8, 8),
        ("hex 3", 8, 9, 8, 8, 8, 9),
        ("hex 4", 9, 8, 8, 8, 9, 8),
        ("hex 5", 8, 9, 8, 9, 9, 9),
        ("hex 6", 9, 9, 9, 8, 9, 8),
        ("hex 7", 8, 8, 8, 8, 9, 8),
        ("hex 8", 8, 9, 8, 8, 8, 8),
        ("hex 9", 9, 9, 8, 9, 9, 9),
        ("hex 10", 9, 9, 9, 8, 9, 9),
        ("hex 11", 8, 8, 8, 9, 9, 9),
        ("hex 12", 9, 9, 9, 8, 8, 8),
        ("hex 13", 9, 9, 9, 9, 8, 9),
        ("hex 14", 9, 8, 9, 9, 9, 9),
        ("hex 15", 8, 8, 8, 9, 8, 8),
        ("hex 16", 8, 8, 9, 8, 8, 8),
        ("hex 17", 8, 9, 9, 8, 8, 9),
        ("hex 18", 9, 8, 8, 9, 9, 8),
        ("hex 19", 8, 8, 8, 8, 9, 9),
        ("hex 20", 9, 9, 8, 8, 8, 8),
        ("hex 21", 9, 8, 9, 8, 8, 9),
        ("hex 22", 9, 8, 8, 9, 8, 9),
        ("hex 23", 9, 8, 8, 8, 8, 8),
        ("hex 24", 8, 8, 8, 8, 8, 9),
        ("hex 25", 9, 9, 9, 8, 8, 9),
        ("hex 26", 9, 8, 8, 9, 9, 9),
        ("hex 27", 9, 8, 8, 8, 8, 9),
        ("hex 28", 8, 9, 9, 9, 9, 8),
        ("hex 29", 8, 9, 8, 8, 9, 8),
        ("hex 30", 9, 8, 9, 9, 8, 9),
        ("hex 31", 8, 9, 9, 9, 8, 8),
        ("hex 32", 8, 8, 9, 9, 9, 8),
        ("hex 33", 9, 9, 9, 9, 8, 8),
        ("hex 34", 8, 8, 9, 9, 9, 9),
        ("hex 35", 9, 8, 9, 8, 8, 8),
        ("hex 36", 8, 8, 8, 9, 8, 9),
        ("hex 37", 9, 9, 8, 9, 8, 9),
        ("hex 38", 9, 8, 9, 8, 9, 9),
        ("hex 39", 8, 9, 8, 9, 8, 8),
        ("hex 40", 8, 8, 9, 8, 9, 8),
        ("hex 41", 9, 8, 8, 8, 9, 9),
        ("hex 42", 9, 9, 8, 8, 8, 9),
        ("hex 43", 8, 9, 9, 9, 9, 9),
        ("hex 44", 9, 9, 9, 9, 9, 8),
        ("hex 45", 8, 9, 9, 8, 8, 8),
        ("hex 46", 8, 8, 8, 9, 9, 8),
        ("hex 47", 8, 9, 9, 8, 9, 8),
        ("hex 48", 8, 9, 8, 9, 9, 8),
        ("hex 49", 8, 9, 9, 9, 8, 9),
        ("hex 50", 9, 8, 9, 9, 9, 8),
        ("hex 51", 8, 8, 9, 8, 8, 9),
        ("hex 52", 9, 8, 8, 9, 8, 8),
        ("hex 53", 9, 9, 8, 9, 8, 8),
        ("hex 54", 8, 8, 9, 8, 9, 9),
        ("hex 55", 8, 8, 9, 9, 8, 9),
        ("hex 56", 9, 8, 9, 9, 8, 8),
        ("hex 57", 9, 9, 8, 9, 9, 8),
        ("hex 58", 8, 9, 9, 8, 9, 9),
        ("hex 59", 9, 9, 8, 8, 9, 8),
        ("hex 60", 8, 9, 8, 8, 9, 9),
        ("hex 61", 9, 9, 8, 8, 9, 9),
        ("hex 62", 8, 8, 9, 9, 8, 8),
        ("hex 63", 8, 9, 8, 9, 8, 9),
        ("hex 64", 9, 8, 9, 8, 9, 8),
    ]

    for hexagram in hexagram_data:
        if (
            hexagram[1] == sixther
            and hexagram[2] == fifther
            and hexagram[3] == fourther
            and hexagram[4] == thirder
            and hexagram[5] == seconder
            and hexagram[6] == firster
        ):
            return hexagram[0]

    return "Not found"

pierwszy = find_hex(sixther, fifther, fourther, thirder, seconder, firster)


def convert_value_2nd(value):
    if value == 6:
        return 9
    elif value == 7:
        return 9
    elif value == 8:
        return 8
    elif value == 9:
        return 8
    else:
        return value


sixtherst = convert_value_2nd(sixth)
fiftherst = convert_value_2nd(fifth)
fourtherst = convert_value_2nd(fourth)
thirderst = convert_value_2nd(third)
seconderst = convert_value_2nd(second)
firsterst = convert_value_2nd(first)


def find_hex2(sixtherst, fiftherst, fourtherst, thirderst, seconderst, firsterst):
    hexagram_data = [
        ("hex 1", 9, 9, 9, 9, 9, 9),
        ("hex 2", 8, 8, 8, 8, 8, 8),
        ("hex 3", 8, 9, 8, 8, 8, 9),
        ("hex 4", 9, 8, 8, 8, 9, 8),
        ("hex 5", 8, 9, 8, 9, 9, 9),
        ("hex 6", 9, 9, 9, 8, 9, 8),
        ("hex 7", 8, 8, 8, 8, 9, 8),
        ("hex 8", 8, 9, 8, 8, 8, 8),
        ("hex 9", 9, 9, 8, 9, 9, 9),
        ("hex 10", 9, 9, 9, 8, 9, 9),
        ("hex 11", 8, 8, 8, 9, 9, 9),
        ("hex 12", 9, 9, 9, 8, 8, 8),
        ("hex 13", 9, 9, 9, 9, 8, 9),
        ("hex 14", 9, 8, 9, 9, 9, 9),
        ("hex 15", 8, 8, 8, 9, 8, 8),
        ("hex 16", 8, 8, 9, 8, 8, 8),
        ("hex 17", 8, 9, 9, 8, 8, 9),
        ("hex 18", 9, 8, 8, 9, 9, 8),
        ("hex 19", 8, 8, 8, 8, 9, 9),
        ("hex 20", 9, 9, 8, 8, 8, 8),
        ("hex 21", 9, 8, 9, 8, 8, 9),
        ("hex 22", 9, 8, 8, 9, 8, 9),
        ("hex 23", 9, 8, 8, 8, 8, 8),
        ("hex 24", 8, 8, 8, 8, 8, 9),
        ("hex 25", 9, 9, 9, 8, 8, 9),
        ("hex 26", 9, 8, 8, 9, 9, 9),
        ("hex 27", 9, 8, 8, 8, 8, 9),
        ("hex 28", 8, 9, 9, 9, 9, 8),
        ("hex 29", 8, 9, 8, 8, 9, 8),
        ("hex 30", 9, 8, 9, 9, 8, 9),
        ("hex 31", 8, 9, 9, 9, 8, 8),
        ("hex 32", 8, 8, 9, 9, 9, 8),
        ("hex 33", 9, 9, 9, 9, 8, 8),
        ("hex 34", 8, 8, 9, 9, 9, 9),
        ("hex 35", 9, 8, 9, 8, 8, 8),
        ("hex 36", 8, 8, 8, 9, 8, 9),
        ("hex 37", 9, 9, 8, 9, 8, 9),
        ("hex 38", 9, 8, 9, 8, 9, 9),
        ("hex 39", 8, 9, 8, 9, 8, 8),
        ("hex 40", 8, 8, 9, 8, 9, 8),
        ("hex 41", 9, 8, 8, 8, 9, 9),
        ("hex 42", 9, 9, 8, 8, 8, 9),
        ("hex 43", 8, 9, 9, 9, 9, 9),
        ("hex 44", 9, 9, 9, 9, 9, 8),
        ("hex 45", 8, 9, 9, 8, 8, 8),
        ("hex 46", 8, 8, 8, 9, 9, 8),
        ("hex 47", 8, 9, 9, 8, 9, 8),
        ("hex 48", 8, 9, 8, 9, 9, 8),
        ("hex 49", 8, 9, 9, 9, 8, 9),
        ("hex 50", 9, 8, 9, 9, 9, 8),
        ("hex 51", 8, 8, 9, 8, 8, 9),
        ("hex 52", 9, 8, 8, 9, 8, 8),
        ("hex 53", 9, 9, 8, 9, 8, 8),
        ("hex 54", 8, 8, 9, 8, 9, 9),
        ("hex 55", 8, 8, 9, 9, 8, 9),
        ("hex 56", 9, 8, 9, 9, 8, 8),
        ("hex 57", 9, 9, 8, 9, 9, 8),
        ("hex 58", 8, 9, 9, 8, 9, 9),
        ("hex 59", 9, 9, 8, 8, 9, 8),
        ("hex 60", 8, 9, 8, 8, 9, 9),
        ("hex 61", 9, 9, 8, 8, 9, 9),
        ("hex 62", 8, 8, 9, 9, 8, 8),
        ("hex 63", 8, 9, 8, 9, 8, 9),
        ("hex 64", 9, 8, 9, 8, 9, 8),
    ]

    for hexagramm in hexagram_data:
        if (
            hexagramm[1] == sixtherst
            and hexagramm[2] == fiftherst
            and hexagramm[3] == fourtherst
            and hexagramm[4] == thirderst
            and hexagramm[5] == seconderst
            and hexagramm[6] == firsterst
        ):
            return hexagramm[0]

    return "Not found"

drugi = find_hex2(sixtherst, fiftherst, fourtherst, thirderst, seconderst, firsterst)


#DICTIONARY PART
# to do: adjust the trigrams icons to corrected hexagrams

hexagram_dict = {
    "hex 1": {
        "icon": "\n☰\n☰",
        "full_name": "乾 (qián) - The Creative (Creative Power)",
        "summary": "A time of great potential and power. The universe is in motion, and it is a moment for action and progress."
    },
    "hex 2": {
        "icon": "\n☷\n☷",
        "full_name": "坤 (kūn) - The Receptive (Natural Response)",
        "summary": "A time to be open and receptive. Embrace the qualities of motherhood and nurture. Seek stability and grounding."
    },
    "hex 3": {
        "icon": "\n☰\n☳",
        "full_name": "屯 (zhūn) - Difficulty at the Beginning",
        "summary": "A time of challenges and obstacles. Stay resolute and gather inner strength. Perseverance will lead to progress."
    },
    "hex 4": {
        "icon": "\n☰\n☷",
        "full_name": "蒙 (méng) - Youthful Folly (Inexperience)",
        "summary": "A time of immaturity and inexperience. Approach situations with caution and seek guidance from wiser individuals."
    },
    "hex 5": {
        "icon": "\n☰\n☳",
        "full_name": "需 (xū) - Waiting (Nourishment)",
        "summary": "A time to be patient and nurture your inner resources. Be prepared for future opportunities."
    },
    "hex 6": {
        "icon": "\n☰\n☷",
        "full_name": "訟 (sòng) - Conflict",
        "summary": "A time of conflict and disagreement. Seek resolution through communication and compromise."
    },
    "hex 7": {
        "icon": "\n☰\n☳",
        "full_name": "師 (shī) - The Army (Collective Force)",
        "summary": "A time to form alliances and work together towards a common goal. Unity and discipline are essential."
    },
    "hex 8": {
        "icon": "\n☰\n☷",
        "full_name": "比 (bǐ) - Holding Together (Union)",
        "summary": "A time of harmony and cooperation. Embrace the power of synergy."
    },
    "hex 9": {
        "icon": "\n☰\n☳",
        "full_name": "小畜 (xiǎo chù) - The Taming Power of the Small (Restrained)",
        "summary": "A time to nurture small, gradual progress. Be patient and accumulate strength."
    },
    "hex 10": {
        "icon": "\n☰\n☷",
        "full_name": "履 (lǚ) - Treading (Conduct)",
        "summary": "A time to be cautious and considerate in your actions. Take one step at a time."
    },
    "hex 11": {
        "icon": "\n☰\n☳",
        "full_name": "泰 (tài) - Peace (Prospering)",
        "summary": "A time of peace and harmony. Embrace the present moment and enjoy stability."
    },
    "hex 12": {
        "icon": "\n☰\n☷",
        "full_name": "否 (pǐ) - Standstill (Stagnation)",
        "summary": "A time of stagnation and lack of progress. Reflect on your situation and seek ways to break free from obstacles."
    },
    "hex 13": {
        "icon": "\n☰\n☳",
        "full_name": "同人 (tóng rén) - Fellowship (Community)",
        "summary": "A time to connect with others and form meaningful bonds. Shared visions will lead to success."
    },
    "hex 14": {
        "icon": "\n☰\n☷",
        "full_name": "大有 (dà yǒu) - Abundance (Sovereignty)",
        "summary": "A time of abundance and prosperity. Embrace the flow of positive energy."
    },
    "hex 15": {
        "icon": "\n☰\n☳",
        "full_name": "谦 (qiān) - Modesty (Moderation)",
        "summary": "A time to be humble and modest in your actions. Avoid arrogance and ego."
    },
    "hex 16": {
        "icon": "\n☰\n☷",
        "full_name": "豫 (yù) - Enthusiasm (Harmonize)",
        "summary": "A time of enthusiasm and optimism. Embrace the energy of change and progress."
    },
    "hex 17": {
        "icon": "\n☰\n☳",
        "full_name": "随 (suí) - Following (Adapting)",
        "summary": "A time to adapt and follow the flow of events. Flexibility will lead to success."
    },
    "hex 18": {
        "icon": "\n☰\n☷",
        "full_name": "蠱 (gǔ) - Work on the Decayed (Repair)",
        "summary": "A time to address and heal old wounds and problems. Transformation is possible."
    },
    "hex 19": {
        "icon": "\n☰\n☳",
        "full_name": "臨 (lín) - Approach (Promotion)",
        "summary": "A time of preparation and careful planning. Approach new endeavors with thoughtfulness."
    },
    "hex 20": {
        "icon": "\n☰\n☷",
        "full_name": "觀 (guān) - Contemplation",
        "summary": "A time of introspection and inner reflection. Seek clarity and understanding."
    },
    "hex 21": {
        "icon": "\n☰\n☳",
        "full_name": "噬嗑 (shì kè) - Biting Through (Reform)",
        "summary": "A time to confront and break through obstacles and challenges. Perseverance is key."
    },
    "hex 22": {
        "icon": "\n☰\n☷",
        "full_name": "賁 (bì) - Grace",
        "summary": "A time of elegance and beauty. Embrace refinement and cultivate your inner grace."
    },
    "hex 23": {
        "icon": "\n☰\n☳",
        "full_name": "剝 (bō) - Splitting Apart (Deterioration)",
        "summary": "A time of disintegration and change. Let go of what no longer serves you and embrace the new."
    },
    "hex 24": {
        "icon": "\n☰\n☷",
        "full_name": "復 (fù) - Return (The Turning Point)",
        "summary": "A time of turning points and new beginnings. Embrace change and be open to transformation."
    },
    "hex 25": {
        "icon": "\n☰\n☳",
        "full_name": "無妄 (wú wàng) - Innocence (The Unexpected)",
        "summary": "A time of innocence and spontaneity. Be open to surprises and unexpected opportunities."
    },
    "hex 26": {
        "icon": "\n☰\n☷",
        "full_name": "大畜 (dà chù) - The Taming Power of the Great (Potential Energy)",
        "summary": "A time of great potential and control. Channel your energies wisely and stay focused."
    },
    "hex 27": {
        "icon": "\n☰\n☳",
        "full_name": "頤 (yí) - Corners of the Mouth (Providing Nourishment)",
        "summary": "A time of nourishment and care. Provide for yourself and others with compassion and generosity."
    },
    "hex 28": {
        "icon": "\n☰\n☷",
        "full_name": "大過 (dà guò) - Preponderance of the Great (Critical Mass)",
        "summary": "A time of excess and extravagance. Be cautious and avoid overindulgence."
    },
    "hex 29": {
        "icon": "\n☰\n☳",
        "full_name": "坎 (kǎn) - The Abysmal (Danger)",
        "summary": "A time of deep emotions and introspection. Embrace the depths of your feelings and seek clarity."
    },
    "hex 30": {
        "icon": "\n☰\n☷",
        "full_name": "離 (lí) - The Clinging (Synergy)",
        "summary": "A time of passion and intensity. Embrace the fire within you and use it wisely."
    },
    "hex 31": {
        "icon": "\n☰\n☳",
        "full_name": "咸 (xián) - Influence (Attraction)",
        "summary": "A time of harmony and attraction. Build connections and seek mutual benefits."
    },
    "hex 32": {
        "icon": "\n☰\n☷",
        "full_name": "恆 (héng) - Duration (Continuing)",
        "summary": "A time of stability and lasting relationships. Cultivate long-term goals and commitment."
    },
    "hex 33": {
        "icon": "\n☰\n☳",
        "full_name": "遯 (dùn) - Retreat",
        "summary": "A time to step back and observe. Gather your strength and prepare for future actions."
    },
    "hex 34": {
        "icon": "\n☰\n☷",
        "full_name": "大壯 (dà zhuàng) - The Power of the Great",
        "summary": "A time of great power and strength. Embrace your capabilities and assertiveness."
    },
    "hex 35": {
        "icon": "\n☰\n☳",
        "full_name": "晉 (jìn) - Progress",
        "summary": "A time of progress and growth. Move forward with confidence and determination."
    },
    "hex 36": {
        "icon": "\n☰\n☷",
        "full_name": "明夷 (míng yí) - Darkening of the Light (Censorship)",
        "summary": "A time of adversity and darkness. Stay strong and find light in the midst of challenges."
    },
    "hex 37": {
        "icon": "\n☰\n☳",
        "full_name": "家人 (jiā rén) - The Family (The Clan)",
        "summary": "A time of family and community. Nurture and support your loved ones."
    },
    "hex 38": {
        "icon": "\n☰\n☷",
        "full_name": "睽 (kuí) - Opposition (Contradiction)",
        "summary": "A time of opposition and conflict. Seek balance and understanding to overcome challenges."
    },
    "hex 39": {
        "icon": "\n☰\n☳",
        "full_name": "蹇 (jiǎn) - Obstruction (Obstacles)",
        "summary": "A time of obstacles and difficulties. Persevere and find creative solutions."
    },
    "hex 40": {
        "icon": "\n☰\n☷",
        "full_name": "解 (xiè) - Deliverance (Liberation)",
        "summary": "A time of liberation and freedom. Embrace positive changes and new opportunities."
    },
    "hex 41": {
        "icon": "\n☰\n☳",
        "full_name": "損 (sǔn) - Decrease (Decline)",
        "summary": "A time of loss and reduction. Let go of what is no longer needed and focus on what matters most."
    },
    "hex 42": {
        "icon": "\n☰\n☷",
        "full_name": "益 (yì) - Increase (Benefit)",
        "summary": "A time of growth and expansion. Embrace abundance and be open to receiving more."
    },
    "hex 43": {
        "icon": "\n☰\n☳",
        "full_name": "夬 (guài) - Breakthrough (Resolution)",
        "summary": "A time of decisive action and breakthroughs. Seize opportunities and be bold in your endeavors."
    },
    "hex 44": {
        "icon": "\n☰\n☷",
        "full_name": "姤 (gòu) - Coming to Meet (Temptation)",
        "summary": "A time of convergence and alignment. Connect with others and find common ground."
    },
    "hex 45": {
        "icon": "\n☰\n☳",
        "full_name": "萃 (cuì) - Gathering Together (Assembling)",
        "summary": "A time of gathering resources and like-minded individuals. Pool your strengths for a common purpose."
    },
    "hex 46": {
        "icon": "\n☰\n☷",
        "full_name": "升 (shēng) - Pushing Upward (Advancement)",
        "summary": "A time of rising and progress. Embrace growth and elevate your aspirations."
    },
    "hex 47": {
        "icon": "\n☰\n☳",
        "full_name": "困 (kùn) - Oppression (Adversity)",
        "summary": "A time of oppression and exhaustion. Find ways to restore balance and vitality."
    },
    "hex 48": {
        "icon": "\n☰\n☷",
        "full_name": "井 (jǐng) - The Well (The Source)",
        "summary": "A time of abundance and sustenance. Tap into your inner resources and nourish yourself."
    },
    "hex 49": {
        "icon": "\n☰\n☳",
        "full_name": "革 (gé) - Revolution (Changing)",
        "summary": "A time of major changes and transformation. Embrace the opportunities for renewal."
    },
    "hex 50": {
        "icon": "\n☰\n☷",
        "full_name": "鼎 (dǐng) - The Cauldron (Cosmic Order)",
        "summary": "A time of gathering and cooperation. Work together to achieve common goals."
    },
    "hex 51": {
        "icon": "\n☰\n☳",
        "full_name": "震 (zhèn) - The Arousing (Shocking)",
        "summary": "A time of awakening and action. Embrace the energy of thunder and take decisive steps."
    },
    "hex 52": {
        "icon": "\n☰\n☷",
        "full_name": "艮 (gèn) - Keeping Still (Meditation)",
        "summary": "A time of stillness and reflection. Find your center and maintain inner peace."
    },
    "hex 53": {
        "icon": "\n☰\n☳",
        "full_name": "漸 (jiàn) - Development (Gradual Progress)",
        "summary": "A time of gradual progress and advancement. Stay persistent and be patient."
    },
    "hex 54": {
        "icon": "\n☰\n☷",
        "full_name": "歸妹 (guī mèi) - The Marrying Maiden (Subordinate)",
        "summary": "A time of union and harmony. Embrace partnerships and celebrate love."
    },
    "hex 55": {
        "icon": "\n☰\n☳",
        "full_name": "豐 (fēng) - Abundance (Zenith)",
        "summary": "A time of great abundance and prosperity. Embrace the flow of positive energy."
    },
    "hex 56": {
        "icon": "\n☰\n☷",
        "full_name": "旅 (lǚ) - The Wanderer (Traveling)",
        "summary": "A time of exploration and travel. Embrace new experiences and broaden your horizons."
    },
    "hex 57": {
        "icon": "\n☰\n☳",
        "full_name": "巽 (xùn) - The Gentle (Penetrating Influence)",
        "summary": "A time of gentleness and adaptability. Embrace the qualities of the wind and be flexible."
    },
    "hex 58": {
        "icon": "\n☰\n☷",
        "full_name": "兌 (duì) - The Joyous (Encouraging)",
        "summary": "A time of joy and celebration. Embrace positivity and share your happiness with others."
    },
    "hex 59": {
        "icon": "\n☰\n☳",
        "full_name": "渙 (huàn) - Dispersion (Reuniting)",
        "summary": "A time of dispersion and release. Let go of what is no longer needed and welcome change."
    },
    "hex 60": {
        "icon": "䷻",
        "full_name": "節 (jié) - Limitation",
        "summary": "A time of limitations and boundaries. Exercise restraint and discipline."
    },
    "hex 61": {
        "icon": "䷼",
        "full_name": "中孚 (zhōng fú) - Inner Truth (Insight)",
        "summary": "A time of sincerity and trust. Stay true to yourself and others."
    },
    "hex 62": {
        "icon": "䷽",
        "full_name": "小過 (xiǎo guò) - Small Preponderance (Conscientiousness)",
        "summary": "A time of minor excesses and imbalance. Seek moderation and find harmony."
    },
    "hex 63": {
        "icon": "䷾",
        "full_name": "既濟 (jì jì) - After Completion (After the End)",
        "summary": "A time of fulfillment and completion. Celebrate your achievements and prepare for new cycles."
    },
    "hex 64": {
        "icon": "䷿",
        "full_name": "未濟 (wèi jì) - Before Completion (Before the End)",
        "summary": "A time of transition and preparation. Gather your strength and make final preparations before moving forward."
    }
}

#RESULT Section

def print_changed_lines(lines):
    line_names = ["sixth", "fifth", "fourth", "third", "second", "first"]
    changed_lines = [line_names[i] for i, value in enumerate(lines) if value in [6, 9]]
    return changed_lines

lines = [sixth, fifth, fourth, third, second, first]

changed_lines = print_changed_lines(lines)


pierwszy_icon = hexagram_dict.get(pierwszy, {}).get("icon", "Icon not available")
pierwszy_full_name = hexagram_dict.get(pierwszy, {}).get("full_name", "Unknown")
pierwszy_summary = hexagram_dict.get(pierwszy, {}).get("summary", "Summary not available")

drugi_icon = hexagram_dict.get(drugi, {}).get("icon", "Icon not available")
drugi_full_name = hexagram_dict.get(drugi, {}).get("full_name", "Unknown")
drugi_summary = hexagram_dict.get(drugi, {}).get("summary", "Summary not available")

def generate_hexagram_url(hexagram_number, source):
    base_urls = {
        "source1": "https://divination.com/iching/lookup/",
        "source2": "https://deoxy.org/iching/",
        "source3": "https://www.psychic-revelation.com/reference/i_l/i_ching/hexagram"
    }

    base_url = base_urls.get(source)
    if not base_url:
        raise ValueError(f"Invalid source: {source}")

    url = f"{base_url}{str(hexagram_number)}"
    if source == "source1":
        url += "-2/"
    else:
        url += ".html"

    return url

hexagram_1_number = int(pierwszy.split()[-1])
hexagram_2_number = int(drugi.split()[-1])
url1 = generate_hexagram_url(hexagram_1_number, "source1")
url2 = generate_hexagram_url(hexagram_2_number, "source1")
url3 = generate_hexagram_url(hexagram_1_number, "source2")
url4 = generate_hexagram_url(hexagram_2_number, "source2")
url5 = generate_hexagram_url(hexagram_1_number, "source3")
url6 = generate_hexagram_url(hexagram_2_number, "source3")

print(f"\nYou will find the answers below.\n")

print(f"YOUR FIRST HEXAGRAM is: {str(hexagram_1_number)}")
#print(f"{pierwszy_icon}")
hex1(zbior)

print(f"\nThis is your current situation:\n{pierwszy_full_name}: {pierwszy_summary}")

print("More info about it (and the changing lines):")
print(url1)
print(url3)
print(url5)

print("\nThe reason for the change are the following lines: " + ", ".join(changed_lines) +".")

print(f"\nYOUR SECOND HEXAGRAM (after the change) is: {str(hexagram_2_number)}")
#print(f"{drugi_icon}")
hex2(zbior)

print(f"\nAnd this is a situation after the change will happen:\n{drugi_full_name}: {drugi_summary}")

print("More info about it:")
print(url2)
print(url4)
print(url6)



#BING Section
import urllib.parse
import webbrowser

def generate_bing_url(prompt, question, hexagram_1_number, hexagram_2_number, reason, source):
    base_url = "https://www.bing.com/search"
    query_params = {
        "q": f"{prompt}, question ({question}) First hexagram ({hexagram_1_number}), second hexagram ({hexagram_2_number}), reason for change ({reason}), sources ({source})"
    }
    url = f"{base_url}?{urllib.parse.urlencode(query_params)}"
    return url

prompt = "As an I Ching diviner, provide interpretations for my question stated below. Write a paragraph for the current situation, the reasons driving the changes, and the resulting situation after the changes. Limit your research to the sources from websites I provide. Use the following information I provide:\"\n"
reason = "changing lines: " + ", ".join(changed_lines) +"."
source = url1 + " " + url3 + " " + url5 + " " + url2 + " " + url4 + " " + url6

url = generate_bing_url(prompt, question, hexagram_1_number, hexagram_2_number, reason, source)

print("\nClick on URL below for a personalized interpretation from Bing Chat (paste it in the Edge browser address bar:")
print(url)

#concatenating the output
output_block = f"Your question was: {question}\n\n" \
f"YOUR FIRST HEXAGRAM is: {str(hexagram_1_number)}\n" \
f"This is your current situation:\n{pierwszy_full_name}: {pierwszy_summary}\n" \
"More info about it (and the changing lines):\n" \
f"{url1}\n{url3}\n{url5}\n" \
"\nThe reason for the change are the following lines: " + ", ".join(changed_lines) + ".\n" \
f"\nYOUR SECOND HEXAGRAM (after the change) is: {str(hexagram_2_number)}\n" \
f"And this is a situation after the change will happen:\n{drugi_full_name}: {drugi_summary}\n" \
"More info about it:\n" \
f"{url2}\n{url4}\n{url6}\n" \
f"\nYou can get personalized interpretation from Bing AI here:\n" \
f"{url}"

#exporting

def save_to_html(output_block):
    # Generate the default filename
    now = datetime.now()
    formatted_date_time = now.strftime("%Y-%m-%d_%H-%M-%S")  # Replace spaces with underscores
    default_filename = f"Iching_interpretation_{formatted_date_time}.html"

    # Define the path to save the file in the user's home directory
    save_path = Path.home() / default_filename

    with open(save_path, "w", encoding='utf-8') as file:
        file.write("<html><body>\n")
        lines = output_block.split("\n")
        for line in lines:
            if line.startswith("http"):
                file.write(f'<a href="{line}">{line}</a><br/>\n')
            else:
                file.write(f"{line}<br/>\n")
        file.write("</body></html>")
    
#display(HTML(f"Output saved at: <a href='{save_path.as_posix()}' target='_blank'>{save_path.as_posix()}</a>"))  # Display as clickable link

    # Open the file in the default web browser
    webbrowser.open(save_path.as_uri())

# Assuming you have the 'output_block' variable from the previous code block
save_to_html(output_block)
