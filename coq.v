Inductive day : Type :=
  | monday
  | tuesday
  | wednesday
  | thursday
  | friday
  | saturday
  | sunday.
  
  
 Definition next_weekday (d:day) : day :=
   match d with
   | monday => tuesday
   | tuesday => wednesday
   | wednesday => thursday
   | thursday => friday
   | friday => monday
   | saturday => monday
   | sunday => monday
   end.
   
Compute next_weekday (monday).
Compute next_weekday (next_weekday(monday)).

Example text_next_weekday:
  (next_weekday(next_weekday saturday)) = tuesday.
  Proof. simpl. reflexivity. Qed.

Inductive bool : Type :=
  | true
  | false.
  
Definition negb (b1:bool) (b2:bool) : bool :=
  match b1 with
  | true => false
  | false => true
  end.

Definition andb (b1:bool) (b2:bool) : bool :=
  match b1 with
   | true => b2
   | false => false
   end.

Definition orb (b1:bool) (b2:bool) : bool :=
  match b1 with
  | true => true
  | false => b2
  end.
  
Example test_orb1: (orb true false) = true.
Proof. simpl. reflexivity. Qed.
Example test_orb2: (orb false false) = false.
Proof. simpl. reflexivity. Qed.
Example test_orb3: (orb false true) = true.
Proof. simpl. reflexivity. Qed.
Example test_orb4: (orb true true) = true.
Proof. simpl. reflexivity. Qed.

Notation "x && y" := (andb x y).
Notation "x || y" := (orb x y).

Example test_orb5: false || false || true = true.
Proof. simpl. reflexivity. Qed.

Definition nandb (b1:bool) (b2:bool) : bool :=
  match b1, b2 with
  | true, true => false
  | _, _ => true
  end.


Check true.

Inductive rgb : Type :=
  | red
  | green
  | blue.
  
Inductive color : Type :=
  | black
  | white
  | primary (p : rgb).
  
Definition monochrome (c:color): bool :=
  match c with
  | black => true
  | white => true
  | primary p => false
  end.
  
Definition isred (c : color) : bool :=
  match c with
  | black => false
  | white => false
  | primary red => true
  | primary _ => false
  end.
  
Module Playground.
  Definition b : rgb := blue.
End Playground.

Definition b : bool := true.

Check Playground.b : rgb.
Check b : bool.

Module TuplePlayground.

Inductive bit : Type :=
  | B0
  | B1.

Inductive nibble : Type :=
  | bits (B0 B1 B2 B3 : bit).
 
Check (bits B1 B0 B1 B0).

Definition all_zero (nb: nibble) : bool :=
  match nb with
  | (bits B0 B0 B0 B0) => true
  | (bits _ _ _ _ ) => false
  end.

Compute (all_zero (bits B1 B0 B1 B0)).
Compute (all_zero (bits B0 B0 B0 B0)).
