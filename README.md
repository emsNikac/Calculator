# Twitter Clone (Mobile + API)

A simplified Twitter/X clone built as a learning project, featuring authentication, tweets, likes, retweets, and follow/unfollow functionality.

---

## Project Structure

This repository contains both the backend API and the mobile application in a single monorepo-style structure:

- **twitter-backend/** – NestJS REST API  
- **twitter-mobile/** – React Native (Expo) mobile app  

The mobile app communicates with the backend via a REST API secured using JWT authentication.

---

## Running the Project Locally

### Requirements

Make sure you have the following installed:

- Node.js (v18+ recommended)
- npm or yarn
- Expo CLI
- Android Studio (Android emulator) or a physical device
- Git

---

## Backend (NestJS API)

```bash
cd twitter-backend
npm install
npm run start:dev
```
---
The backend will start on:
http://localhost:3000

Backend Responsibilities
	•	User authentication (JWT)
	•	User profiles
	•	Follow / unfollow users
	•	Tweets, likes, and retweets
	•	Feed generation

Note: The backend uses in-memory storage (no database).

---

## Mobile App (React Native + Expo)
```bash
cd twitter-mobile
npm install
npx expo start
```
Then:
	•	Press a to open the Android emulator
	•	Press i to open the iOS emulator
	•	Or scan the QR code with Expo Go on your phone

### Android Emulator Networking

- When running on an Android emulator, the app uses http://10.0.2.2:3000 to access the local backend

---

## Architecture Overview

Backend Architecture
	•	NestJS feature-based modules
	•	Controllers, services, and DTOs
	•	JWT authentication
	•	RESTful API design
	•	No database (in-memory state)

Mobile Architecture
	•	React Native with Expo
	•	Context API for global state:
	•	AuthContext (authentication & user state)
	•	TweetsContext (feed & tweet actions)
	•	Axios API layer
	•	React Navigation (Auth stack & App stack)
	•	Clear separation of:
	•	Screens
	•	Components
	•	API logic
	•	Context/state

---

## Features
	•	User registration & login
	•	JWT-based authentication
	•	Create tweets
	•	Like tweets
	•	Retweet tweets
	•	Follow & unfollow users
	•	User profiles with followers/following count
	•	Feed with retweets and engagement state
	•	Logout functionality






