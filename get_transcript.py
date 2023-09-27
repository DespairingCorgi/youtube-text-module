from youtube_transcript_api import YouTubeTranscriptApi
import youtube_transcript_api

VIDEOID = 'dFRXcYJVfMM'

def check_transcript_list(vid):
    '''
        vid: videoid
        
        this function checks all available transcript from the video corresponding vid
    '''
    print(YouTubeTranscriptApi.list_transcripts(vid))

def get_transcripts(vid, *langs):
    '''
        vid: videoid
        *langs: language list
        
        caution: this function only collects manual transcription from the video corresponding vid.
    '''
    transcript_list =  YouTubeTranscriptApi.list_transcripts(vid)
    d = {}
    for lang in langs:
        try:
            transcript = transcript_list.find_manually_created_transcript([lang])
            transcriptdata = transcript.fetch()
        except youtube_transcript_api.NoTranscriptFound as e:
            print("the video does not contain {lang} transcription")
            continue        
        texts = [timedtranscript['text'].replace('\n', ' ') for timedtranscript in transcriptdata]
        d[lang] = texts
    return d

# d = get_transcripts(VIDEOID, 'ko', 'en')
# print(d['ko'])
# print(d['en'])
