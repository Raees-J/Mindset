// Sample Surah data with Tafsir
// In production, this would come from API

export interface SurahData {
  number: number;
  name: string;
  english_name: string;
  meaning: string;
  verses_count: number;
  revelation_place: string;
  overview: string;
  verses: Array<{
    ayah_number: number;
    arabic_text: string;
    translation: string;
    tafsir: string;
  }>;
}

export const SURAHS: SurahData[] = [
  {
    number: 1,
    name: "الفاتحة",
    english_name: "Al-Fatihah",
    meaning: "The Opening",
    verses_count: 7,
    revelation_place: "Makkah",
    overview: "Al-Fatihah is the opening chapter of the Quran and is recited in every unit of the Muslim prayer. It is a comprehensive prayer that includes praise of Allah, acknowledgment of His sovereignty, a request for guidance, and a plea to be among those who have earned His favor. This Surah encapsulates the essence of the entire Quran.",
    verses: [
      {
        ayah_number: 1,
        arabic_text: "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
        translation: "In the name of Allah, the Entirely Merciful, the Especially Merciful.",
        tafsir: "The Bismillah emphasizes Allah's mercy and compassion. Rahman (Entirely Merciful) refers to Allah's mercy that encompasses all creation, while Rahim (Especially Merciful) refers to His specific mercy for believers in the Hereafter."
      },
      {
        ayah_number: 2,
        arabic_text: "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
        translation: "All praise is due to Allah, Lord of the worlds.",
        tafsir: "This verse teaches us to praise Allah for all His blessings. 'Lord of the worlds' means Allah is the Creator, Sustainer, and Master of everything that exists - humans, jinn, angels, and all creation."
      },
      {
        ayah_number: 3,
        arabic_text: "الرَّحْمَٰنِ الرَّحِيمِ",
        translation: "The Entirely Merciful, the Especially Merciful.",
        tafsir: "The repetition of Allah's mercy emphasizes its importance. His mercy precedes His wrath, and it is through His mercy that we have hope for forgiveness and Paradise."
      },
      {
        ayah_number: 4,
        arabic_text: "مَالِكِ يَوْمِ الدِّينِ",
        translation: "Sovereign of the Day of Recompense.",
        tafsir: "This reminds us of the Day of Judgment when Allah alone will judge all creation. This awareness should motivate us to live righteously and prepare for that inevitable day."
      },
      {
        ayah_number: 5,
        arabic_text: "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ",
        translation: "It is You we worship and You we ask for help.",
        tafsir: "This is the core of Islamic monotheism (Tawheed). We worship Allah alone and seek help from Him alone. This verse teaches us to balance between worship and reliance on Allah."
      },
      {
        ayah_number: 6,
        arabic_text: "اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ",
        translation: "Guide us to the straight path.",
        tafsir: "The straight path is Islam - the path of truth, righteousness, and guidance. We ask for this guidance daily because we constantly need Allah's help to stay on the right path."
      },
      {
        ayah_number: 7,
        arabic_text: "صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ",
        translation: "The path of those upon whom You have bestowed favor, not of those who have evoked [Your] anger or of those who are astray.",
        tafsir: "Those favored are the prophets, truthful ones, martyrs, and righteous. Those who earned anger are those who knew the truth but rejected it. Those astray are those who were ignorant and did not seek guidance. We ask Allah to keep us on the path of the favored ones."
      }
    ]
  },
  {
    number: 112,
    name: "الإخلاص",
    english_name: "Al-Ikhlas",
    meaning: "The Sincerity",
    verses_count: 4,
    revelation_place: "Makkah",
    overview: "Surah Al-Ikhlas is a concise yet profound declaration of Islamic monotheism (Tawheed). Despite being one of the shortest chapters, the Prophet Muhammad (peace be upon him) said it is equivalent to one-third of the Quran because it deals with the fundamental concept of Allah's oneness and His attributes. This Surah was revealed in response to questions about Allah's nature.",
    verses: [
      {
        ayah_number: 1,
        arabic_text: "قُلْ هُوَ اللَّهُ أَحَدٌ",
        translation: "Say, 'He is Allah, [who is] One.'",
        tafsir: "This verse establishes the absolute oneness of Allah. 'Ahad' means One in a unique, absolute sense - there is no one like Him, no partner, no equal. This is the foundation of Islamic belief."
      },
      {
        ayah_number: 2,
        arabic_text: "اللَّهُ الصَّمَدُ",
        translation: "Allah, the Eternal Refuge.",
        tafsir: "'As-Samad' means the Self-Sufficient Master whom all creatures need. He needs no one, but everyone needs Him. He is eternal, without beginning or end, perfect in every way."
      },
      {
        ayah_number: 3,
        arabic_text: "لَمْ يَلِدْ وَلَمْ يُولَدْ",
        translation: "He neither begets nor is born.",
        tafsir: "Allah is not born from anything, nor does He give birth to anything. This negates any concept of Allah having children or parents, distinguishing Islamic monotheism from other beliefs."
      },
      {
        ayah_number: 4,
        arabic_text: "وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ",
        translation: "Nor is there to Him any equivalent.",
        tafsir: "Nothing and no one is comparable to Allah in any way. He is unique in His essence, attributes, and actions. This verse completes the description of Allah's absolute uniqueness."
      }
    ]
  },
  {
    number: 113,
    name: "الفلق",
    english_name: "Al-Falaq",
    meaning: "The Daybreak",
    verses_count: 5,
    revelation_place: "Makkah",
    overview: "Surah Al-Falaq is one of the two protective chapters (along with An-Nas) known as Al-Mu'awwidhatayn. The Prophet (peace be upon him) would recite these before sleep for protection. This Surah teaches us to seek Allah's refuge from various forms of evil, both physical and spiritual.",
    verses: [
      {
        ayah_number: 1,
        arabic_text: "قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ",
        translation: "Say, 'I seek refuge in the Lord of daybreak.'",
        tafsir: "We seek protection from Allah, the Lord who brings forth the daybreak, splitting darkness with light. This symbolizes His power over all creation and His ability to protect us from all harm."
      },
      {
        ayah_number: 2,
        arabic_text: "مِن شَرِّ مَا خَلَقَ",
        translation: "From the evil of that which He created.",
        tafsir: "We seek protection from the evil of all created things - harmful creatures, evil people, jinn, and any source of harm in creation."
      },
      {
        ayah_number: 3,
        arabic_text: "وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ",
        translation: "And from the evil of darkness when it settles.",
        tafsir: "This refers to the evil that emerges in the darkness of night, including harmful creatures and evil forces that become active after sunset."
      },
      {
        ayah_number: 4,
        arabic_text: "وَمِن شَرِّ النَّفَّاثَاتِ فِي الْعُقَدِ",
        translation: "And from the evil of the blowers in knots.",
        tafsir: "This refers to those who practice magic and sorcery, blowing on knots while casting spells. We seek Allah's protection from their evil and harm."
      },
      {
        ayah_number: 5,
        arabic_text: "وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ",
        translation: "And from the evil of an envier when he envies.",
        tafsir: "Envy (hasad) is when someone wishes for the removal of blessings from others. We seek protection from the harm that envious people may cause through their evil eye or actions."
      }
    ]
  }
];

export function searchSurahs(query: string): SurahData[] {
  const lowerQuery = query.toLowerCase();
  return SURAHS.filter(surah => 
    surah.english_name.toLowerCase().includes(lowerQuery) ||
    surah.name.includes(query) ||
    surah.number.toString() === query ||
    surah.meaning.toLowerCase().includes(lowerQuery)
  );
}
