package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class Base32Test {

    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void encodeBase32() {
        assertEquals("1",Base32.encodeBase32(1,1));
        assertEquals("1",Base32.encodeBase32(1,-1));
        assertEquals("-1",Base32.encodeBase32(-1,1));
        assertEquals("-1",Base32.encodeBase32(-1,-1));
        System.out.println("testis here");

        assertEquals("-10",Base32.encodeBase32(-32,-1));
    }

    @Test
    public void encodeBase321() {
        assertEquals("000000000001",Base32.encodeBase32(1));
        assertEquals("-000000000001",Base32.encodeBase32(-1));
    }

    @Test
    public void decodeBase32() {
        assertEquals(42,Base32.decodeBase32("1b"));
        assertEquals(-42,Base32.decodeBase32("-1b"));
        try{
            assertEquals(-1,Base32.decodeBase32("a"));
        }catch (IllegalArgumentException e){
            e.printStackTrace();
        }
    }

    @Test
    public void getCharIndex() {
        assertEquals(1,Base32.getCharIndex('1'));
        try{
            assertEquals("not a base32 character: " + 'a',Base32.getCharIndex('a'));
        }catch (IllegalArgumentException e){
            System.out.print(e);
        }
    }

    @Test
    public void padLeftWithZerosToLength() {
        assertEquals("0abc",Base32.padLeftWithZerosToLength("abc",4));
        assertEquals("abc",Base32.padLeftWithZerosToLength("abc",-4));
    }
}