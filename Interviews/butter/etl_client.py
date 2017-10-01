"""
Requirement 1: the output of run() must be a JSON string.
See test_requirement_1
Requirement 2: the output of run() must be a JSON string, specifically:
    A JSON dictionary, containing:
        'doc-count': integer, the number of documents received
        'error-count': integer, the number of errors received
        'docs': a JSON dictionary:
            keys are document ID strings
            values are arrays of words in the document
See test_requirement_2
Requirement 3: all words in output of run() must be lower-cased
See test_requirement_3
Requirement 4: exclude these words from the word arrays: and or not but to in
See test_requirement_4
Requirement 5: handle RetryImmediatelyError.
At times handle_request() may raise RetryImmediatelyError.
Do not count the error against the number of requests to run.
Re-try the operation (by calling the service's handle_request() again).
Include the number of errors in the output as in Requirement 2.
See test_requirement_5
Requirement 6:
Handle 'update' responses from the service, which have the form:
    {'operation': 'update',
     'document': {
        'id': string, the document id
        'data': string, updated document data
     }}
Expect the document ID to match a document previously sent in an 'add' response.
Replace the document data for that ID with the new data.
See test_requirement_6
Requirement 7:
Handle 'delete' responses from the service, which have the form:
    {'operation': 'delete',
     'document-id': string, the document id}
Expect the document ID to match a document previously sent in an 'add' response.
Remove the document data for that ID with the new data.
See test_requirement_7
"""

import IPython as ipy
import json
from document_service import DocumentService, RetryImmediatelyError

class ETLClient:

    def __init__(self):
        self.documents = {}
        self.error_count = 0
        self.stop_words = ['and', 'or', 'not', 'but', 'to', 'in']
        self.dispatcher = {
            'add': self._add_or_update_doc,
            'update': self._add_or_update_doc,
            'delete': self._remove_doc
        }

    def _increment_error_count(self):
        self.error_count += 1

    def _filter(self, words):
        return filter(lambda word: word not in self.stop_words, words.lower().split())

    def _add_or_update_doc(self, event):
        self.documents[event['document']['id']] = self._filter(event['document']['data'])

    # def _update_doc(self, event):
    #     self.documents[event['document']['id']] = self._filter(event['document']['data'])

    def _remove_doc(self, event):
        del self.documents[event['document-id']]

    def response(self):
        data = {}
        data['doc-count'] = len(self.documents)
        data['error-count'] = self.error_count
        data['docs'] = self.documents
        return json.dumps(data)

    def run(self, service, max_requests):
        """
        Handle max_requests calls to the given DocumentService.
        RetryImmediatelyError should be silently ignored and should *not*
        count as a request.
        Return document list.
        """
        for i in range(0, max_requests):
            try:
                event = service.handle_request()
                self.dispatcher[event['operation']](event)
            except RetryImmediatelyError:
                self._increment_error_count()
                event = service.handle_request()
                self.dispatcher[event['operation']](event)
        return self.response()