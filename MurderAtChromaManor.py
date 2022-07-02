title = "A Murder at Chroma Manor"
setting = "As your car pulls up the long drive, the imposing manor comes into view. It appears weathered and faded, " \
          "but stoic and solid. Detective Sergeant Lewis appears to be waiting just outside the grand entrance for you."
det_sergeant = "Detective Sergeant Lewis"
intro = 'Scratching his head, Detective Sergeant Lewis says, “We have an unusual situation for you to investigate ' \
        'today. A gunshot was heard and everyone came running to find Col. Jasper Chroma dead with a gun on the ' \
        'floor behind him, and Capt. Lavender was seated in the next chair. One of the witnesses called it in saying ' \
        'they had the suspect, and were going to lock the door to the scene of the crime. When Constable Bredon ' \
        'arrived, he found signs that multiple attempts on the victim’s life were made with various methods. What’s ' \
        'more, Medical Examiner Stevenson says the shot is unlikely to have killed him. The question seems to be who ' \
        'didn’t try to kill him. The witnesses are all in the conservatory and we took the housekeeper’s keys and ' \
        'locked all the other doors until we can do a thorough search.'
primary_menu = {
    1: 'Examine the scene of the crime',
    2: 'Question the primary suspect',
    3: 'Examine the other rooms in the manor',
    4: 'Question the other witnesses'
}
scene_desc = 'The study is a comfortable room with wood paneling on the walls. As you enter, Detective Sergeant ' \
             'Lewis says, “Mind your step, sir. We’ve left everything as we found it.” He points to an old military ' \
             'service revolver lying on the floor in front of a large wooden desk with tarnished iron pulls. ' \
             'Centered on the wall behind the desk is a large oil portrait of a man in full military dress next to ' \
             'a striking young woman in a flowing gown. A display cabinet and a bookcase flank the portrait. ' \
             'Opposite the desk, there are two comfortable and well-used chairs placed in front of the fireplace ' \
             'with a small table within easy reach. The fireplace is almost as imposing although more ornate than ' \
             'the desk. Above the fireplace hangs a portrait of a family: a slightly older version of the man and ' \
             'woman from the other portrait surrounded by two boys and a girl.'
scene_menu = {
    1: 'Examination of the body',
    2: 'Examination of the fireplace area',
    3: 'Examination of the desk area'
}
body_desc = 'The two chairs sit at angles where two people in them could easily talk but also easily watch the fire. ' \
            'The chair with it’s back to the door contains a frail man in slightly faded clothes suiting the lord ' \
            'of the manor. Medical Examiner Stevenson, points to a small gash on the man’s temple, and says, ' \
            '“That’s a gunshot wound. Just grazed it, and it should have bled like you wouldn’t believe, but ' \
            'unlikely to be fatal if attended to. However, no blood means he was likely already dead. Tell the ' \
            'boys to look for the bullet either in the fireplace or near the door to determine where the shooter ' \
            'was standing.” A black handle sticks out of the victim’s side slightly obscured by his arm lying limp ' \
            'on the armrest of the chair. When the medical examiner carefully lifts the arm, the man’s hand has a ' \
            'smudge of ink that appears to be fairly recent. He pulls the black handle out of the man’s side, ' \
            'revealing a blood-soaked, sharp chef’s knife. “Here we have a stabbing. Plenty of blood here. Most ' \
            'likely the cause of death.” The medical examiner lifts the head to reveal indentations in the neck. ' \
            'He says with a heavy sigh, “and here we have strangulation from some sort of braided or twisted cord. ' \
            'The man was likely already dead or dying. Normally there would be more swelling and the texture of the ' \
            'cord wouldn’t be as clear if it had been done while he was alive.” Detective Sergeant Lewis says, ' \
            '“See what I mean? Overkill.”'
body_menu = {
    1: 'Examination of the gun',
    2: 'Examination of the contents of the victim\'s pockets'
}
gun_exam = 'It appears to have been recently fired. It is fully loaded except for one bullet. There is a bit of dust ' \
           'on one side as if it had been set down somewhere dusty.'
pocket_exam = 'Several brass keys, a small iron key and a small ornate silver key on a ring. A separate brass key, ' \
              'similar to those on the ring, with a leather cord. A monogrammed lighter. A pocket watch.'
pocket_menu = {
    1: 'Examination of the brass keys on the ring',
    2: 'Examination of the small iron key',
    3: 'Examination of the ornate silver key',
    4: 'Examination of the brass key on the leather cord',
    5: 'Examination of the lighter',
    6: 'Examination of the pocket watch'
}
brass_keys_exam =
iron_key_exam =
silver_key_exam =
brass_key_exam =
lighter_exam =
watch_exam = 'This pocket watch is well worn and has a Colonel\'s crest embossed on the outside. A picture has been ' \
             'stuck into the inside of the watch cover. The lady in the picture resembles a young version of the lady ' \
             'in the two portraits in the room.'
fireplace_desc = 'Between the comfortable chairs sits a small table with a silver tray. Upon the tray is an ' \
                 'ashtray, cigar box, an amber-colored liquid in an almost full decanter and in a snifter glass, ' \
                 'as well as a rich honey-colored liquid in a half-full decanter and in a whiskey glass. '
fireplace_menu = {
    1: 'Examination of the snifter glass',
    2: 'Examination of the whiskey glass',
    3: 'Examination of the fireplace'
}
snifter_exam = 'Carefully sniffing the liquor in the snifter glass reveals it to be expensive brandy.  However, the ' \
               'color is not quite right for that caliber of brandy and you notice some odd sediment in the bottom. ' \
               'Looking at the decanter, it appears the same. Detective Sergeant Lewis: “What’s this? I see what ' \
               'caught your attention sir. I will have the boys test it.” Shaking his head as he scribbles in his ' \
               'book. “Given the other circumstances, we’ll be lucky if it isn’t poison of some kind.”'
whiskey_exam = ''
fireplace_exam


desk_desc =
desk_menu = {
    1: 'Examination of the locked drawer',
    2: 'Examination of the bookcase',
    3: 'Examination of the display case'
}
drawer_menu = {
    1: 'Examination of the will',
    2: 'Examination of the letter',
    3: 'Examination of the key',
    4: 'Examination of the bank book',
    5: 'Examination of the wallet'
}
will_menu = {
    1: 'Bequest to Cerise Chroma',
    2: 'Bequest to Kelly Chroma',
    3: 'Bequest to Azure Chroma',
    4: 'Bequest to Captain William Lavender',
    5: 'Bequest to Housekeeper Myrtle Snow',
    6: 'Bequest to personal physician'
}
bookcase_menu = {
    1: '',
    2: ''
}
display_menu = {
    1: '',
    2: ''
}
pri_susp_main_menu = {
    1: 'Before I ask any questions, do you have any statement you would like to make?',
    2: 'Tell me exactly what happened in the study.',
    3: 'We’re hoping you can help explain a few things. What can you tell us about the day’s events?'
}
pri_susp_sub_menu = {
    1: 'Your shot didn\'t kill him. In fact, it seems we was dead for sometime before.',
    2: 'We only found one gunshot wound. A grazing head shot.'
}
rooms_menu = {
    1: '',
    2: ''
}
witnesses_menu = {
    1: '',
    2: ''
}
_menu = {
    1: '',
    2: ''
}
