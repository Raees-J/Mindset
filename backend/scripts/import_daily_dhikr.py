"""
Import daily dhikr and meaningful hadiths about Prophet's daily recitations
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from db.session import SessionLocal, engine
from models.database import Base, Hadith
from services.vector_store import VectorStoreService

def import_daily_dhikr():
    """Import daily dhikr hadiths"""
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        # Initialize vector store
        vector_store = VectorStoreService()
        
        daily_dhikr_hadiths = [
            # POST-SALAH DHIKR
            {
                "arabic_text": "مَنْ قَرَأَ آيَةَ الْكُرْسِيِّ دُبُرَ كُلِّ صَلَاةٍ مَكْتُوبَةٍ لَمْ يَمْنَعْهُ مِنْ دُخُولِ الْجَنَّةِ إِلَّا أَنْ يَمُوتَ",
                "english_translation": "Whoever recites Ayatul Kursi after every obligatory prayer, nothing prevents him from entering Paradise except death.",
                "reference": "Sunan an-Nasa'i 9928 (Sahih)",
                "category": "dhikr",
                "theme": "post-salah",
                "context": "The Prophet ﷺ taught this powerful practice. Ayatul Kursi (2:255) is the greatest verse in the Quran, and reciting it after each of the five daily prayers guarantees Paradise.",
                "practical_application": "After saying 'Assalamu alaikum wa rahmatullah' to complete your salah, recite Ayatul Kursi. This takes less than 30 seconds but has immense reward."
            },
            {
                "arabic_text": "مَنْ سَبَّحَ اللَّهَ فِي دُبُرِ كُلِّ صَلَاةٍ ثَلَاثًا وَثَلَاثِينَ وَحَمِدَ اللَّهَ ثَلَاثًا وَثَلَاثِينَ وَكَبَّرَ اللَّهَ ثَلَاثًا وَثَلَاثِينَ فَتْلِكَ تِسْعَةٌ وَتِسْعُونَ وَقَالَ تَمَامَ الْمِائَةِ لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ غُفِرَتْ خَطَايَاهُ وَإِنْ كَانَتْ مِثْلَ زَبَدِ الْبَحْرِ",
                "english_translation": "Whoever glorifies Allah (says Subhan Allah) 33 times after every prayer, praises Allah (says Alhamdulillah) 33 times, and magnifies Allah (says Allahu Akbar) 33 times, that is 99, then completes 100 by saying 'La ilaha illallahu wahdahu la sharika lah, lahul mulku wa lahul hamd, wa huwa 'ala kulli shay'in qadir' - his sins will be forgiven even if they are like the foam of the sea.",
                "reference": "Sahih Muslim 597",
                "category": "dhikr",
                "theme": "post-salah",
                "context": "This is the Tasbih that the Prophet ﷺ taught for after every fardh prayer. It takes about 2 minutes and wipes away sins.",
                "practical_application": "Count on your fingers: 33 Subhan Allah, 33 Alhamdulillah, 33 Allahu Akbar, then once: La ilaha illallahu wahdahu la sharika lah, lahul mulku wa lahul hamd, wa huwa 'ala kulli shay'in qadir."
            },
            
            # MORNING ADHKAR
            {
                "arabic_text": "مَنْ قَالَ حِينَ يُصْبِحُ وَحِينَ يُمْسِي سُبْحَانَ اللَّهِ وَبِحَمْدِهِ مِائَةَ مَرَّةٍ لَمْ يَأْتِ أَحَدٌ يَوْمَ الْقِيَامَةِ بِأَفْضَلَ مِمَّا جَاءَ بِهِ إِلَّا أَحَدٌ قَالَ مِثْلَ مَا قَالَ أَوْ زَادَ عَلَيْهِ",
                "english_translation": "Whoever says 'Subhan Allahi wa bihamdihi' (Glory and praise be to Allah) 100 times in the morning and evening, no one will come on the Day of Resurrection with anything better than what he brings, except one who has said the same or more.",
                "reference": "Sahih Muslim 2692",
                "category": "dhikr",
                "theme": "morning-evening",
                "context": "The Prophet ﷺ emphasized this simple dhikr. It takes only 2-3 minutes but brings immense reward.",
                "practical_application": "Say 'Subhan Allahi wa bihamdihi' 100 times after Fajr and 100 times after Maghrib or Isha. Use a tasbih counter or your fingers."
            },
            {
                "arabic_text": "مَنْ قَالَ لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ فِي يَوْمٍ مِائَةَ مَرَّةٍ كَانَتْ لَهُ عَدْلَ عَشْرِ رِقَابٍ وَكُتِبَتْ لَهُ مِائَةُ حَسَنَةٍ وَمُحِيَتْ عَنْهُ مِائَةُ سَيِّئَةٍ وَكَانَتْ لَهُ حِرْزًا مِنَ الشَّيْطَانِ يَوْمَهُ ذَلِكَ حَتَّى يُمْسِيَ",
                "english_translation": "Whoever says 'La ilaha illallahu wahdahu la sharika lah, lahul mulku wa lahul hamd, wa huwa 'ala kulli shay'in qadir' 100 times a day, it will be equivalent to freeing 10 slaves, 100 good deeds will be written for him, 100 bad deeds will be erased, and it will be a protection from Shaitan for that day until evening.",
                "reference": "Sahih al-Bukhari 3293, Sahih Muslim 2691",
                "category": "dhikr",
                "theme": "morning-evening",
                "context": "This powerful dhikr gives multiple rewards: freedom from sins, protection from Shaitan, and the reward of freeing slaves.",
                "practical_application": "Recite this 100 times in the morning. It takes about 5 minutes and protects you all day."
            },
            {
                "arabic_text": "مَنْ قَالَ حِينَ يُصْبِحُ اللَّهُمَّ مَا أَصْبَحَ بِي مِنْ نِعْمَةٍ أَوْ بِأَحَدٍ مِنْ خَلْقِكَ فَمِنْكَ وَحْدَكَ لَا شَرِيكَ لَكَ فَلَكَ الْحَمْدُ وَلَكَ الشُّكْرُ فَقَدْ أَدَّى شُكْرَ يَوْمِهِ",
                "english_translation": "Whoever says in the morning: 'Allahumma ma asbaha bi min ni'matin aw bi-ahadin min khalqika faminka wahdaka la sharika lak, falakal hamdu wa lakash-shukr' (O Allah, whatever blessing I or any of Your creation have risen upon, it is from You alone, without partner, so for You is all praise and unto You all thanks) - he has fulfilled the thanks due for that day.",
                "reference": "Sunan Abi Dawud 5073 (Sahih)",
                "category": "dhikr",
                "theme": "morning-evening",
                "context": "The Prophet ﷺ taught this as a way to fulfill our obligation of gratitude to Allah for all His blessings.",
                "practical_application": "Say this once every morning after Fajr. It acknowledges that everything good comes from Allah alone."
            },
            
            # EVENING ADHKAR
            {
                "arabic_text": "مَنْ قَالَ حِينَ يُمْسِي أَمْسَيْنَا وَأَمْسَى الْمُلْكُ لِلَّهِ وَالْحَمْدُ لِلَّهِ لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ رَبِّ أَسْأَلُكَ خَيْرَ مَا فِي هَذِهِ اللَّيْلَةِ وَخَيْرَ مَا بَعْدَهَا وَأَعُوذُ بِكَ مِنْ شَرِّ مَا فِي هَذِهِ اللَّيْلَةِ وَشَرِّ مَا بَعْدَهَا",
                "english_translation": "Whoever says in the evening: 'We have reached the evening and the dominion belongs to Allah, and praise is for Allah. There is none worthy of worship except Allah, alone, without partner. To Him belongs the dominion and to Him is praise, and He is over all things competent. My Lord, I ask You for the good of this night and the good after it, and I seek refuge in You from the evil of this night and the evil after it' - Allah will grant him the good of that night.",
                "reference": "Sahih Muslim 2723",
                "category": "dhikr",
                "theme": "morning-evening",
                "context": "This evening dhikr seeks Allah's protection and blessings for the night ahead.",
                "practical_application": "Recite this once after Maghrib or before sleeping. In the morning, replace 'amsayna' with 'asbahna' (we have reached morning)."
            },
            
            # BEFORE SLEEP
            {
                "arabic_text": "كَانَ النَّبِيُّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ إِذَا أَوَى إِلَى فِرَاشِهِ كُلَّ لَيْلَةٍ جَمَعَ كَفَّيْهِ ثُمَّ نَفَثَ فِيهِمَا فَقَرَأَ فِيهِمَا قُلْ هُوَ اللَّهُ أَحَدٌ وَقُلْ أَعُوذُ بِرَبِّ الْفَلَقِ وَقُلْ أَعُوذُ بِرَبِّ النَّاسِ ثُمَّ يَمْسَحُ بِهِمَا مَا اسْتَطَاعَ مِنْ جَسَدِهِ يَبْدَأُ بِهِمَا عَلَى رَأْسِهِ وَوَجْهِهِ وَمَا أَقْبَلَ مِنْ جَسَدِهِ يَفْعَلُ ذَلِكَ ثَلَاثَ مَرَّاتٍ",
                "english_translation": "When the Prophet ﷺ went to bed every night, he would hold his palms together, spit in them softly, and recite Surah Al-Ikhlas, Al-Falaq, and An-Nas. Then he would wipe over as much of his body as he could, starting with his head, face, and the front of his body. He would do this three times.",
                "reference": "Sahih al-Bukhari 5017",
                "category": "dhikr",
                "theme": "before-sleep",
                "context": "This was the Prophet's ﷺ nightly routine for protection. These three surahs protect from all evil, envy, and harm.",
                "practical_application": "Before sleeping: 1) Cup your hands, 2) Blow gently into them, 3) Recite the three Quls (Ikhlas, Falaq, Nas), 4) Wipe over your body starting from your head. Repeat 3 times."
            },
            {
                "arabic_text": "إِذَا أَتَيْتَ مَضْجَعَكَ فَتَوَضَّأْ وُضُوءَكَ لِلصَّلَاةِ ثُمَّ اضْطَجِعْ عَلَى شِقِّكَ الْأَيْمَنِ ثُمَّ قُلْ اللَّهُمَّ أَسْلَمْتُ وَجْهِي إِلَيْكَ وَفَوَّضْتُ أَمْرِي إِلَيْكَ وَأَلْجَأْتُ ظَهْرِي إِلَيْكَ رَغْبَةً وَرَهْبَةً إِلَيْكَ لَا مَلْجَأَ وَلَا مَنْجَا مِنْكَ إِلَّا إِلَيْكَ اللَّهُمَّ آمَنْتُ بِكِتَابِكَ الَّذِي أَنْزَلْتَ وَبِنَبِيِّكَ الَّذِي أَرْسَلْتَ",
                "english_translation": "When you go to bed, perform wudu as for prayer, then lie on your right side and say: 'O Allah, I submit my face to You, I entrust my affairs to You, I turn my back in reliance upon You, in hope and fear of You. There is no refuge or escape from You except to You. I believe in Your Book which You revealed and Your Prophet whom You sent.' If you die that night, you will die upon the fitrah (natural state of Islam).",
                "reference": "Sahih al-Bukhari 247, Sahih Muslim 2710",
                "category": "dhikr",
                "theme": "before-sleep",
                "context": "The Prophet ﷺ taught this to ensure that if death comes during sleep, one dies in a state of complete submission to Allah.",
                "practical_application": "Make wudu before bed, lie on your right side, and recite this dua. It's a beautiful way to end each day in complete trust in Allah."
            },
            
            # GENERAL DAILY DHIKR
            {
                "arabic_text": "كَلِمَتَانِ خَفِيفَتَانِ عَلَى اللِّسَانِ ثَقِيلَتَانِ فِي الْمِيزَانِ حَبِيبَتَانِ إِلَى الرَّحْمَنِ سُبْحَانَ اللَّهِ وَبِحَمْدِهِ سُبْحَانَ اللَّهِ الْعَظِيمِ",
                "english_translation": "Two words that are light on the tongue, heavy on the Scale, and beloved to the Most Merciful: 'Subhan Allahi wa bihamdihi, Subhan Allahil-Azim' (Glory and praise be to Allah, Glory be to Allah the Magnificent).",
                "reference": "Sahih al-Bukhari 6406, Sahih Muslim 2694",
                "category": "dhikr",
                "theme": "anytime",
                "context": "The Prophet ﷺ said these are the most beloved words to Allah. They're easy to say but carry immense weight on the Day of Judgment.",
                "practical_application": "Repeat this throughout your day - while walking, driving, cooking, or waiting. It takes 2 seconds but fills your scale with good deeds."
            },
            {
                "arabic_text": "مَنْ قَالَ سُبْحَانَ اللَّهِ وَبِحَمْدِهِ فِي يَوْمٍ مِائَةَ مَرَّةٍ حُطَّتْ خَطَايَاهُ وَإِنْ كَانَتْ مِثْلَ زَبَدِ الْبَحْرِ",
                "english_translation": "Whoever says 'Subhan Allahi wa bihamdihi' 100 times a day, his sins will be forgiven even if they are like the foam of the sea.",
                "reference": "Sahih al-Bukhari 6405, Sahih Muslim 2691",
                "category": "dhikr",
                "theme": "anytime",
                "context": "This simple dhikr wipes away sins no matter how many they are. The Prophet ﷺ encouraged doing it daily.",
                "practical_application": "Set a goal to say this 100 times daily. It takes 3-5 minutes and cleanses you of sins."
            },
            {
                "arabic_text": "أَحَبُّ الْكَلَامِ إِلَى اللَّهِ أَرْبَعٌ سُبْحَانَ اللَّهِ وَالْحَمْدُ لِلَّهِ وَلَا إِلَهَ إِلَّا اللَّهُ وَاللَّهُ أَكْبَرُ",
                "english_translation": "The most beloved words to Allah are four: Subhan Allah (Glory be to Allah), Alhamdulillah (Praise be to Allah), La ilaha illallah (There is no god but Allah), and Allahu Akbar (Allah is the Greatest).",
                "reference": "Sahih Muslim 2137",
                "category": "dhikr",
                "theme": "anytime",
                "context": "These four phrases are the most beloved to Allah. The Prophet ﷺ said it doesn't matter which one you start with.",
                "practical_application": "Keep your tongue moist with these four phrases throughout the day. They're the best words you can say."
            },
            
            # ENTERING/LEAVING HOME
            {
                "arabic_text": "إِذَا دَخَلَ الرَّجُلُ بَيْتَهُ فَذَكَرَ اللَّهَ عِنْدَ دُخُولِهِ وَعِنْدَ طَعَامِهِ قَالَ الشَّيْطَانُ لَا مَبِيتَ لَكُمْ وَلَا عَشَاءَ",
                "english_translation": "When a man enters his home and remembers Allah upon entering and before eating, Shaitan says (to his followers): 'You have no place to stay and no dinner.'",
                "reference": "Sahih Muslim 2018",
                "category": "dhikr",
                "theme": "daily-routine",
                "context": "Remembering Allah when entering home and before eating keeps Shaitan away from your house and food.",
                "practical_application": "Say 'Bismillah' when entering your home and before eating. This simple act protects your home and food from Shaitan."
            },
            
            # ISTIGHFAR
            {
                "arabic_text": "مَنْ لَزِمَ الِاسْتِغْفَارَ جَعَلَ اللَّهُ لَهُ مِنْ كُلِّ ضِيقٍ مَخْرَجًا وَمِنْ كُلِّ هَمٍّ فَرَجًا وَرَزَقَهُ مِنْ حَيْثُ لَا يَحْتَسِبُ",
                "english_translation": "Whoever persists in seeking forgiveness (Istighfar), Allah will make a way out for him from every difficulty, relief from every worry, and provide for him from sources he never expected.",
                "reference": "Sunan Abi Dawud 1518 (Hasan)",
                "category": "dhikr",
                "theme": "istighfar",
                "context": "The Prophet ﷺ said constant Istighfar opens doors of provision, removes difficulties, and brings unexpected blessings.",
                "practical_application": "Say 'Astaghfirullah' (I seek Allah's forgiveness) frequently throughout the day - aim for 100 times. It solves problems and brings rizq."
            },
            {
                "arabic_text": "كَانَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ يَسْتَغْفِرُ اللَّهَ فِي الْيَوْمِ مِائَةَ مَرَّةٍ",
                "english_translation": "The Messenger of Allah ﷺ used to seek Allah's forgiveness 100 times a day.",
                "reference": "Sahih Muslim 2702",
                "category": "dhikr",
                "theme": "istighfar",
                "context": "Despite being sinless, the Prophet ﷺ sought forgiveness 100 times daily. How much more should we seek forgiveness?",
                "practical_application": "If the Prophet ﷺ sought forgiveness 100 times daily, we should do the same. Say 'Astaghfirullah' 100 times each day."
            },
            
            # SALAWAT ON THE PROPHET
            {
                "arabic_text": "مَنْ صَلَّى عَلَيَّ صَلَاةً صَلَّى اللَّهُ عَلَيْهِ بِهَا عَشْرًا",
                "english_translation": "Whoever sends blessings upon me once, Allah will send blessings upon him ten times.",
                "reference": "Sahih Muslim 408",
                "category": "dhikr",
                "theme": "salawat",
                "context": "Sending salawat (blessings) on the Prophet ﷺ brings 10 blessings from Allah in return.",
                "practical_application": "Say 'Allahumma salli 'ala Muhammad' frequently. Each time you say it once, Allah blesses you 10 times."
            },
            {
                "arabic_text": "أَوْلَى النَّاسِ بِي يَوْمَ الْقِيَامَةِ أَكْثَرُهُمْ عَلَيَّ صَلَاةً",
                "english_translation": "The people most deserving of my intercession on the Day of Resurrection are those who send the most blessings upon me.",
                "reference": "Sunan at-Tirmidhi 484 (Hasan)",
                "category": "dhikr",
                "theme": "salawat",
                "context": "The more you send blessings on the Prophet ﷺ, the closer you'll be to him on the Day of Judgment and more deserving of his intercession.",
                "practical_application": "Make it a habit to send abundant salawat on the Prophet ﷺ daily, especially on Fridays. Aim for at least 100 times."
            },
            
            # FRIDAY SPECIAL
            {
                "arabic_text": "إِنَّ مِنْ أَفْضَلِ أَيَّامِكُمْ يَوْمَ الْجُمُعَةِ فَأَكْثِرُوا عَلَيَّ مِنَ الصَّلَاةِ فِيهِ فَإِنَّ صَلَاتَكُمْ مَعْرُوضَةٌ عَلَيَّ",
                "english_translation": "Among the best of your days is Friday, so send abundant blessings upon me on that day, for your blessings are presented to me.",
                "reference": "Sunan Abi Dawud 1047 (Sahih)",
                "category": "dhikr",
                "theme": "friday",
                "context": "Friday is the best day of the week, and the Prophet ﷺ specifically asked us to send abundant blessings upon him on this day.",
                "practical_application": "On Fridays, increase your salawat on the Prophet ﷺ. Try to send at least 100-300 salawat throughout the day."
            }
        ]
        
        print(f"Importing {len(daily_dhikr_hadiths)} daily dhikr hadiths...")
        
        for hadith_data in daily_dhikr_hadiths:
            # Check if hadith already exists
            existing = db.query(Hadith).filter(
                Hadith.reference == hadith_data["reference"]
            ).first()
            
            if existing:
                print(f"Skipping duplicate: {hadith_data['reference']}")
                continue
            
            # Create hadith
            hadith = Hadith(
                arabic_text=hadith_data["arabic_text"],
                english_translation=hadith_data["english_translation"],
                reference=hadith_data["reference"],
                category=hadith_data["category"],
                theme=hadith_data["theme"],
                context=hadith_data.get("context"),
                practical_application=hadith_data.get("practical_application")
            )
            
            db.add(hadith)
            db.commit()
            db.refresh(hadith)
            
            # Add to vector store
            vector_store.add_hadith(hadith)
            
            print(f"✓ Added: {hadith_data['theme']} - {hadith_data['reference']}")
        
        print(f"\n✅ Successfully imported {len(daily_dhikr_hadiths)} daily dhikr hadiths!")
        print("\nCategories added:")
        print("- Post-Salah Dhikr (Ayatul Kursi, Tasbih)")
        print("- Morning & Evening Adhkar")
        print("- Before Sleep Routine")
        print("- General Daily Dhikr")
        print("- Istighfar (Seeking Forgiveness)")
        print("- Salawat on the Prophet ﷺ")
        print("- Friday Special")
        
    except Exception as e:
        print(f"Error importing daily dhikr: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    import_daily_dhikr()
