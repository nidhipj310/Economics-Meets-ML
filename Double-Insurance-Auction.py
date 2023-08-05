class Participant
  def_init_(self, participant_id):
  self.bids=[] #list to store bids submitted by the participant

  def place_bid(self, coverage_amount, premium_amount):
    self.bids.append((coverage_amount, premium_amount))
  def get_bids(self):
    return self.bids

    class DoubleInsuranceAuction:
        def_init_(self):
            self.participants={}

    def add_participant(self, participant_id)  :
        if participant_id not in self.participants:
            self.participants[participant_id] = Participant(partcipant_id)

    def submit_bid(self, participant_id, coverage_amount, premium_amount):
        if participant_id in self.participants:
            participant=self.participants[participant_id]       
            participant.place_bid(coverage_amount, premium_amount)
            return True
            else: