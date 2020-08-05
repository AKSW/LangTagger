import com.optimaize.languagedetector;

//load all languages:
List<LanguageProfile> languageProfiles = new LanguageProfileReader().readAllBuiltIn();

//build language detector:
LanguageDetector languageDetector = LanguageDetectorBuilder.create(NgramExtractors.standard())
        .withProfiles(languageProfiles)
        .build();

//create a text object factory
TextObjectFactory textObjectFactory = CommonTextObjectFactories.forDetectingOnLargeText();

//query:
TextObject textObject = textObjectFactory.forText("my text");
Optional<LdLocale> lang = languageDetector.detect(textObject);